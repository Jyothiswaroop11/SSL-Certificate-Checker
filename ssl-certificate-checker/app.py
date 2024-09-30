# Copyright (c) 2024 Jyothiswaroop Boggavarapu
# This file is part of SSL-Certificate-Checker, released under the MIT License - see LICENSE file for details.

from concurrent.futures import ThreadPoolExecutor, as_completed
import ssl
import socket
import time
from typing import Optional, Dict, Any, List
from urllib.parse import urlparse
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID
from flask import Flask, json, render_template, request, send_file, jsonify, Response, stream_with_context
import pandas as pd
from io import BytesIO
import os
import re
from dataclasses import dataclass
from collections import defaultdict
import warnings
from cryptography.utils import CryptographyDeprecationWarning
import logging
import traceback

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Config:
    TIMEOUT: int = 5
    MAX_RETRIES: int = 2
    RETRY_DELAY: float = 0.5
    MAX_WORKERS: int = 100
    PORT: int = 443

config = Config()

@dataclass
class CertificateInfo:
    success: bool
    common_name: str
    issuer_by: str
    issuer_to: str
    valid_from: str
    valid_to: str
    exception: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            'Success': self.success,
            'Common Name': self.common_name,
            'Issuer By': self.issuer_by,
            'Issuer To': self.issuer_to,
            'Valid From': self.valid_from,
            'Valid To': self.valid_to,
            'Exception': self.exception
        }

def handle_exception(e: Exception) -> str:
    error_mapping = {
        ssl.SSLError: "SSL Certificate Error",
        ssl.CertificateError: "Certificate Error",
        socket.timeout: "Connection Timeout: The server took too long to respond.",
        socket.gaierror: "DNS Resolution Error",
        socket.error: "Socket Error",
        ConnectionRefusedError: "Connection Refused",
        ConnectionResetError: "Connection Reset",
        ConnectionAbortedError: "Connection Aborted",
        ConnectionError: "Connection Error",
        ValueError: "Value Error",
        OSError: lambda e: "DNS Resolution Error" if 'No address associated with hostname' in str(e) else f"OS Error: {str(e)}",
        PermissionError: "Permission Error",
        FileNotFoundError: "File Not Found Error",
        IOError: "IO Error",
        MemoryError: "Memory Error: Not enough memory to complete the operation.",
        TimeoutError: "Timeout Error: The operation timed out.",
        NotImplementedError: "Not Implemented Error",
        KeyError: "Key Error",
        IndexError: "Index Error",
        AttributeError: "Attribute Error",
        TypeError: "Type Error",
        ImportError: "Import Error",
        RuntimeError: "Runtime Error"
    }
    
    # Handle x509 exceptions separately
    if isinstance(e, x509.base.InvalidVersion):
        return "Invalid X.509 version"
    elif isinstance(e, ValueError) and "Invalid certificate" in str(e):
        return "Invalid certificate"
    
    error_handler = error_mapping.get(type(e), lambda x: f"Unexpected Error: {str(x)}")
    return error_handler(e) if callable(error_handler) else error_handler

def is_ip_address(url: str) -> bool:
    return bool(re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', url))

def format_url(url: str) -> str:
    if is_ip_address(url):
        return url
    if not url.startswith(('https://', 'http://')):
        return f'https://{url}'
    return url

def extract_host_from_url(url: str) -> str:
    if is_ip_address(url):
        return url
    parsed_url = urlparse(url)
    return parsed_url.netloc or parsed_url.path.split('/')[0] or url

def get_certificate(host: str, port: int = config.PORT, timeout: int = config.TIMEOUT) -> Optional[bytes]:
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    context.options |= 0x4  # OP_LEGACY_SERVER_CONNECT

    for attempt in range(config.MAX_RETRIES):
        try:
            with socket.create_connection((host, port), timeout=timeout) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    return ssock.getpeercert(binary_form=True)
        except Exception as e:
            if attempt < config.MAX_RETRIES - 1:
                time.sleep(config.RETRY_DELAY)
                continue
            raise
    raise Exception("Failed to retrieve certificate after all attempts")

def get_certificate_details(url: str) -> CertificateInfo:
    hostname = extract_host_from_url(url)
    port = config.PORT

    try:
        der_cert = get_certificate(hostname, port, config.TIMEOUT)
        if not der_cert:
            raise Exception("Failed to retrieve certificate")

        cert = x509.load_der_x509_certificate(der_cert, default_backend())
        subject = cert.subject.rfc4514_string()
        issuer = cert.issuer.rfc4514_string()
        
        issuer_common_name = next((attribute.value for attribute in cert.issuer if attribute.oid == NameOID.COMMON_NAME), "")

        return CertificateInfo(
            success=True,
            common_name=issuer_common_name,
            issuer_by=issuer,
            issuer_to=subject,
            valid_from=cert.not_valid_before.strftime('%Y-%m-%d %H:%M:%S'),
            valid_to=cert.not_valid_after.strftime('%Y-%m-%d %H:%M:%S'),
            exception=""
        )
    except Exception as e:
        return CertificateInfo(False, "", "", "", "", "", handle_exception(e))

def process_url(row, url, pass_name):
    original_url = url
    formatted_url = format_url(url)
    start_time = time.time()
    try:
        cert_info = get_certificate_details(formatted_url)
        end_time = time.time()
        connection_time = (end_time - start_time) * 1000

        status = 'Pass' if cert_info.success and pass_name.lower() in cert_info.issuer_by.lower() else 'Fail'
        
        result = {
            'S.No': row,
            'URLS': original_url,
            'Modified URLS': formatted_url,
            'Pass/Fail': status,
            'Connection Time (ms)': round(connection_time, 2),
            **cert_info.to_dict()
        }
    except Exception as e:
        result = {
            'S.No': row,
            'URLS': original_url,
            'Modified URLS': formatted_url,
            'Pass/Fail': 'Fail',
            'Connection Time (ms)': 'N/A',
            'Success': False,
            'Exception': str(e)
        }
    
    return result

def process_urls_generator(urls: List[str], pass_name: str):
    with ThreadPoolExecutor(max_workers=config.MAX_WORKERS) as executor:
        future_to_url = {executor.submit(process_url, idx+1, url, pass_name): (idx+1, url) for idx, url in enumerate(urls)}
        for future in as_completed(future_to_url):
            idx, url = future_to_url[future]
            try:
                result = future.result()
                yield result
            except Exception as exc:
                yield {
                    'S.No': idx, 'URLS': url, 'Modified URLS': url, 
                    'Pass/Fail': 'Fail', 'Connection Time (ms)': 'N/A', 
                    'Success': False, 'Exception': f'Error: {exc}'
                }

def process_urls_in_order(urls, pass_name):
    results = []
    start_time = time.time()
    for idx, url in enumerate(urls, start=1):
        result = process_url(idx, url, pass_name)
        results.append(result)
        yield result
    
    end_time = time.time()
    summary = summarize_results(results, start_time, end_time)
    yield {'summary': summary, 'complete': True}

def process_urls(urls: List[str], pass_name: str) -> List[Dict[str, Any]]:
    results = []
    with ThreadPoolExecutor(max_workers=config.MAX_WORKERS) as executor:
        future_to_url = {executor.submit(process_url, idx+1, url, pass_name): (idx+1, url) for idx, url in enumerate(urls)}
        for future in as_completed(future_to_url):
            idx, url = future_to_url[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as exc:
                results.append({
                    'S.No': idx, 'URLS': url, 'Modified URLS': url, 
                    'Pass/Fail': 'Fail', 'Connection Time (ms)': 'N/A', 
                    'Success': False, 'Exception': f'Error: {exc}'
                })
    # Sort the results by S.No
    return sorted(results, key=lambda x: x['S.No'])

def summarize_results(results: List[Dict[str, Any]], start_time: float, end_time: float) -> Dict[str, Any]:
    summary = defaultdict(int)
    total_connection_time = 0
    exceptions = defaultdict(int)

    for result in results:
        summary['total_urls'] += 1
        summary['pass' if result['Pass/Fail'] == 'Pass' else 'fail'] += 1
        
        try:
            connection_time = float(result['Connection Time (ms)'])
            total_connection_time += connection_time
        except (ValueError, TypeError):
            pass

        if result['Exception']:
            exceptions[result['Exception']] += 1

    if summary['total_urls'] > 0:
        summary['average_connection_time_ms'] = f"{round(total_connection_time / summary['total_urls'], 2)} ms"
    else:
        summary['average_connection_time_ms'] = "0 ms"

    summary['exceptions'] = dict(exceptions)
    summary['start_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
    summary['end_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
    summary['execution_time_ms'] = round((end_time - start_time) * 1000, 2)

    return dict(summary)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            pass_name = request.form.get('pass_name', '')
            file = request.files.get('file')
            
            if file and file.filename:
                # File upload logic
                df = pd.read_excel(file) if file.filename.endswith('.xlsx') else pd.read_csv(file)
                urls = df.iloc[:, 0].tolist()  # Assuming URLs are in the first column
            else:
                # Check for manual URL entry
                manual_urls = request.form.get('manualUrls')
                if not manual_urls:
                    return jsonify({'error': 'Please either upload a file or enter URLs manually'}), 400
                urls = [url.strip() for url in manual_urls.split('\n') if url.strip()]

            # Store URLs and pass_name in session or a temporary storage
            app.config['URLS'] = urls
            app.config['PASS_NAME'] = pass_name

            return jsonify({'message': 'Processing started', 'total_urls': len(urls)})

        except Exception as e:
            logger.exception(f"Error processing request: {str(e)}")
            return jsonify({'error': f'Error processing request: {str(e)}\n{traceback.format_exc()}'}), 500

    return render_template('index.html')


@app.route('/process_manual_urls', methods=['POST'])
def process_manual_urls():
    try:
        data = request.json
        urls = data.get('urls', [])
        pass_name = data.get('pass_name', '')
        
        if not urls:
            return jsonify({'error': 'No URLs provided'}), 400

        # Store URLs and pass_name in session or a temporary storage
        app.config['URLS'] = urls
        app.config['PASS_NAME'] = pass_name

        return jsonify({'message': 'Processing started', 'total_urls': len(urls)})

    except Exception as e:
        logger.exception(f"Error processing manual URLs: {str(e)}")
        return jsonify({'error': f'Error processing request: {str(e)}\n{traceback.format_exc()}'}), 500

def process_url(row, url, pass_name=''):
    original_url = url
    formatted_url = format_url(url)
    start_time = time.time()
    try:
        cert_info = get_certificate_details(formatted_url)
        end_time = time.time()
        connection_time = (end_time - start_time) * 1000

        status = 'Pass' if cert_info.success and (not pass_name or pass_name.lower() in cert_info.issuer_by.lower()) else 'Fail'
        
        result = {
            'S.No': row,
            'URLS': original_url,
            'Modified URLS': formatted_url,
            'Pass/Fail': status,
            'Connection Time (ms)': round(connection_time, 2),
            **cert_info.to_dict()
        }
    except Exception as e:
        result = {
            'S.No': row,
            'URLS': original_url,
            'Modified URLS': formatted_url,
            'Pass/Fail': 'Fail',
            'Connection Time (ms)': 'N/A',
            'Success': False,
            'Exception': str(e)
        }
    
    return result

@app.route('/stream')
def stream():
    urls = app.config.get('URLS', [])
    pass_name = app.config.get('PASS_NAME', '')

    if not urls:
        return jsonify({'error': 'No data to process'}), 400

    def generate():
        total_urls = len(urls)
        for index, result in enumerate(process_urls_in_order(urls, pass_name), 1):
            if 'complete' in result:
                yield f"data: {json.dumps(result)}\n\n"
            else:
                progress = (index / total_urls) * 100
                yield f"data: {json.dumps({'result': result, 'progress': progress})}\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

@app.route('/stream_manual')
def stream_manual():
    urls = app.config.get('URLS', [])
    pass_name = app.config.get('PASS_NAME', '')

    if not urls:
        return jsonify({'error': 'No data to process'}), 400

    def generate():
        total_urls = len(urls)
        for index, result in enumerate(process_urls_in_order(urls, pass_name), 1):
            if 'complete' in result:
                yield f"data: {json.dumps(result)}\n\n"
            else:
                progress = (index / total_urls) * 100
                yield f"data: {json.dumps({'result': result, 'progress': progress})}\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

@app.route('/download/<format>', methods=['POST'])
def download_file(format):
    results = request.json.get('results', [])
    summary = request.json.get('summary', {})
    if not results:
        return 'No results found to download', 400
    
    df = pd.DataFrame(results)
    columns_order = ['S.No', 'URLS', 'Modified URLS', 'Pass/Fail', 'Connection Time (ms)', 'Common Name', 'Issuer By', 'Issuer To', 'Valid From', 'Valid To', 'Exception']
    df = df[columns_order]
    
    output = BytesIO()
    
    if format == 'excel':
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Results', index=False)
            
            # Add summary sheet
            summary_data = pd.DataFrame([summary])
            summary_data.to_excel(writer, sheet_name='Summary', index=False)
            
            # Add chart data
            chart_data = pd.DataFrame({
                'Status': ['Pass', 'Fail'],
                'Count': [summary['pass'], summary['fail']]
            })
            chart_data.to_excel(writer, sheet_name='Chart Data', index=False)
            
        mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        filename = 'results.xlsx'
    elif format == 'csv':
        df.to_csv(output, index=False)
        # Append summary and chart data
        output.write(b'\n\nSummary:\n')
        summary_df = pd.DataFrame([summary])
        summary_df.to_csv(output, mode='a', index=False)
        output.write(b'\n\nChart Data:\n')
        chart_data = pd.DataFrame({
            'Status': ['Pass', 'Fail'],
            'Count': [summary['pass'], summary['fail']]
        })
        chart_data.to_csv(output, mode='a', index=False)
        mimetype = 'text/csv'
        filename = 'results.csv'
    elif format == 'txt':
        df.to_csv(output, index=False, sep='\t')
        mimetype = 'text/plain'
        filename = 'results.txt'
    else:
        return 'Invalid format', 400
    
    output.seek(0)
    return send_file(
        output,
        mimetype=mimetype,
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
     app.run()
