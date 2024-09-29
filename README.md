# SSL Certificate Checker

## Overview
The SSL Certificate Checker is a robust web-based tool designed to extract and display SSL certificate details from a list of URLs provided in a file (XLS/XLSX/CSV format). This tool is invaluable for system administrators, developers, and IT professionals who need to ensure that SSL certificates are valid, up-to-date, and properly configured across multiple websites.

## Version History

### Version 3.0 (Latest)
#### New Features and Improvements
- **Automated Startup Process**
  - Batch file for one-click application launch
  - Dynamic source code folder detection
  - Automatic Flask server initiation
  - Chrome browser launch to http://localhost:5000/
  - Synchronized server and batch file termination with browser closure
- **Enhanced Clear Functionality**
  - Improved clear button to terminate ongoing processes
  - Simultaneous clearing of displayed results
- **Advanced Error Reporting**
  - Conditional error display based on error count
  - Streamlined access to comprehensive error list
- **User Interface Refinements**
  - Improved error message presentation
  - Enhanced user guidance for error resolution

#### Key Enhancements
- Simplified application startup and shutdown process
- Improved user control over ongoing operations
- More intuitive error management system
- Enhanced overall user experience with smoother workflow

#### Technical Improvements
- Integration of batch scripting for process automation
- Implementation of browser-server synchronization
- Refined error handling and display logic
- Optimized clear functionality for better resource management

### Version 2.0
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
- Improved exception handling and display in results
- Enhanced clarity and consistency in reporting SSL-related exceptions
- Added more detailed error messages for common SSL certificate issues
- Implemented proper formatting and truncation of long exception messages in the UI

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
- Compare Certificates Side by Side
  - Ability to select multiple certificates for comparison
  - Side-by-side view of selected certificates' details
  - Highlighting of differences between compared certificates

## Key Components
- Web Interface (HTML, CSS, JavaScript with Alpine.js)
- Backend Processing (Python with Flask)
- Data Management
- Visualization (Chart.js)

## Folder Structure
```
ssl-certificate-checker/
│
├── Run_SSL_Checker.bat
│
└── app/
    ├── templates/
    │   └── index.html
    ├── app.py
    ├── LICENSE
    ├── README.md
    └── requirements.txt
```

## How It Works
1. Upload file with URLs
2. Specify expected certificate name
3. Process URLs and retrieve SSL certificate details
4. Display real-time results
5. Download results or view detailed error reports

## Usage
1. Navigate to the `ssl-certificate-checker` folder
2. Double-click the `Run_SSL_Checker.bat` file to start the application
3. Chrome will open automatically to http://localhost:5000
4. Upload file (XLS, XLSX, or CSV) with URLs
5. Enter expected certificate name
6. Click "Submit"
7. Monitor progress bar
8. View results table
9. Use "View All Errors" for comprehensive error list (if more than 5 errors)
10. Customize experience (dark mode, font size)
11. Close Chrome to automatically stop the server and close the batch file

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Google Chrome browser

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/your-username/ssl-certificate-checker.git
   cd ssl-certificate-checker
   ```
2. Navigate to the `app` folder:
   ```
   cd app
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
1. Ensure you are in the main `ssl-certificate-checker` folder
2. Double-click the `Run_SSL_Checker.bat` file to start the application
3. Chrome will automatically open to http://localhost:5000
4. To stop the application, simply close the Chrome window

## Troubleshooting
If you encounter any issues, please check the following:
- Ensure you're using Python 3.7 or higher
- Make sure all dependencies are correctly installed
- Check that you're in the correct directory when running commands
- Verify that the virtual environment is activated when installing dependencies
- Ensure Google Chrome is installed on your system
- Check that the folder structure matches the one described above

For more information or if you encounter any bugs, please open an issue on the GitHub repository.

## License
This project is licensed under the MIT License - see the [LICENSE](app/LICENSE) file for details.

## Contact
For support, feature requests, or any queries, please contact:
- Project Maintainer: Jyothiswaroop Boggavarapu
- Email: bjyothiswaroop7@gmail.com
- GitHub Issues: https://github.com/Jyothiswaroop11/ssl-certificate-checker/issues

We appreciate your feedback to make this tool better!
