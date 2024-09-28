# SSL Certificate Checker

## Overview
The SSL Certificate Checker is a robust web-based tool designed to extract and display SSL certificate details from a list of URLs provided in a file (XLS/XLSX/CSV format). This tool is invaluable for system administrators, developers, and IT professionals who need to ensure that SSL certificates are valid, up-to-date, and properly configured across multiple websites.

## Version History

### Version 2.0 (Latest)

#### New Features and Improvements
- Enhanced Error Handling
- Real-time Progress Updates
- Detailed Error Reporting
- Improved Chart Functionality
- User Interface Enhancements
- Performance Optimization

#### Bug Fixes
- Resolved issues with percentage display in the progress bar
- Fixed error message formatting in the results table
- Corrected chart rendering issues in dark mode

### Version 1.0

#### Features
- File Upload Support (XLS, XLSX, CSV)
- Detailed SSL Certificate Information
- Performance Metrics
- Parallel URL Processing
- Pagination
- Export Options (Excel, CSV, Text)
- Dark Mode Support
- Customizable Font Size
- Execution Summary

## Key Components
- Web Interface (HTML, CSS, JavaScript with Alpine.js)
- Backend Processing (Python with Flask)
- Data Management
- Visualization (Chart.js)

## How It Works
1. Upload file with URLs
2. Specify expected certificate name
3. Process URLs and retrieve SSL certificate details
4. Display real-time results
5. Download results or view detailed error reports

## Usage
1. Upload file (XLS, XLSX, or CSV) with URLs
2. Enter expected certificate name
3. Click "Submit"
4. Monitor progress bar
5. View results table
6. Use "View All Errors" for comprehensive error list
7. Customize experience (dark mode, font size)

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/ssl-certificate-checker.git
   cd ssl-certificate-checker
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Set the Flask application:
   - On Windows:
     ```
     set FLASK_APP=app.py
     ```
   - On macOS and Linux:
     ```
     export FLASK_APP=app.py
     ```

2. (Optional) Enable debug mode:
   - On Windows:
     ```
     set FLASK_ENV=development
     ```
   - On macOS and Linux:
     ```
     export FLASK_ENV=development
     ```

3. Run the Flask application:
   ```
   flask run
   ```

4. Open a web browser and navigate to `http://localhost:5000` to access the SSL Certificate Checker.

### Using the SSL Certificate Checker

1. Prepare a CSV or Excel file containing a list of URLs you want to check.
2. Enter the expected certificate name for validation.
3. Upload your file and click "Submit" to start the SSL certificate checking process.
4. View the results in the web interface or download them in your preferred format.

### Stopping the Application

To stop the Flask server, press `CTRL+C` in the terminal where it's running.

### Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:
```
deactivate
```

## Troubleshooting

If you encounter any issues, please check the following:
- Ensure you're using Python 3.7 or higher.
- Make sure all dependencies are correctly installed.
- Check that you're in the project directory when running commands.
- Verify that the virtual environment is activated when installing dependencies and running the application.

For more information or if you encounter any bugs, please open an issue on the GitHub repository.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Jyothiswaroop11/SSL-Certificate-Checker/blob/main/LICENSE) file for details.

MIT License

Copyright (c) 2024 Jyothiswaroop Boggavarapu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact
For support, feature requests, or any queries, please contact:

- **Project Maintainer:** Jyothiswaroop Boggavarapu
- **Email:** bjyothiswaroop7@gmail.com
- **GitHub Issues:** [https://github.com/Jyothiswaroop11/ssl-certificate-checker/issues](https://github.com/Jyothiswaroop11/ssl-certificate-checker/issues)

We appreciate your feedback to make this tool better!
