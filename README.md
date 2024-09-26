# **SSL Certificate Checker**

## **Overview**

The **SSL Certificate Checker** is a web-based tool designed to extract and display SSL certificate details from a list of URLs provided in a file (XLS/XLSX/CSV format). The tool processes the URLs, validates their SSL certificates, and presents the results in a user-friendly tabular format. This is especially useful for system administrators, developers, and IT professionals who need to ensure that SSL certificates are valid, up-to-date, and properly configured for multiple websites.

## **Features**

- **File Upload Support**: Allows users to upload files in XLS, XLSX, or CSV format containing a list of URLs to check.
- **Detailed SSL Certificate Information**: Displays certificate details like:
  - Common Name (CN)
  - Issuer Details (Issuer By, Issuer To)
  - Validity Period (Valid From, Valid To)
  - Certificate Pass/Fail status
  - Connection Time (ms)
  - Exceptions (if any)
- **Performance Metrics**: Logs the start/end time of execution and calculates the time taken for each connection in milliseconds.
- **Parallel URL Processing**: Enhances performance by processing multiple URLs simultaneously.
- **Pagination**: Provides an easy way to navigate large sets of results with pagination support.
- **Export Options**: Results can be downloaded in multiple formats, including Excel, CSV, PDF, and Text files.
- **Dark Mode Support**: Users can toggle between light and dark modes for better readability.
- **Customizable Font Size**: Users can choose the font size for the displayed data.
- **Execution Summary**: A summary of the execution is displayed after processing, showing key statistics.

## **Key Components**

- **Web Interface**: A clean, responsive GUI built with HTML, CSS, and JavaScript that allows easy interaction with the SSL checker.
- **Backend Processing**: Written in Python, leveraging libraries like `ssl` and `socket` to connect to URLs and fetch certificate details.
- **Data Management**: The input files are processed to extract URLs, and the results are dynamically displayed in a tabular format.

## **How It Works**

1. The user uploads a file containing URLs.
2. The tool processes each URL, retrieving the SSL certificate details and performance metrics.
3. The results are displayed in a table, showing all the relevant information for each URL's SSL certificate.
4. Users can download the results in the preferred format.
5. The tool provides additional features like dark mode, font size customization, and pagination for easy navigation.

## **Usage**

1. Upload a file (XLS, XLSX, or CSV) with a list of URLs to check.
2. Click on the "Upload && Check SSL" button to begin the SSL certificate verification.
3. View the results in the displayed table or download them in your preferred format.
4. Customize your experience using options like dark mode or font size adjustments.

