# SSL Certificate Checker

## Overview
The SSL Certificate Checker is a robust web-based tool designed to extract and display SSL certificate details from a list of URLs provided in a file (XLS/XLSX/CSV format) or entered manually. This tool is invaluable for system administrators, developers, and IT professionals who need to ensure that SSL certificates are valid, up-to-date, and properly configured across multiple websites.

## Version History

### Version 4.0 (Latest)
#### New Features and Improvements
- **Manual URL Entry**
  - Added option to manually enter URLs in addition to file upload
  - Support for up to 1000 manually entered URLs
- **Enhanced User Interface**
  - Improved layout with separate sections for file upload and manual URL entry
  - More intuitive form submission process
- **Advanced Logging System**
  - Implemented a comprehensive logging system with a dedicated log viewer
  - Real-time log updates with auto-scroll functionality
- **Improved Error Handling**
  - Enhanced error detection and reporting for both file uploads and manual URL entries
  - More detailed error messages in the user interface
- **Progress Bar Enhancements**
  - Added visual particles to the progress bar for a more dynamic display
  - Improved progress tracking for manual URL processing
- **Optimized Backend Processing**
  - Refined URL processing logic for better performance
  - Improved handling of various URL formats and edge cases

#### Technical Improvements
- Updated Flask routes to handle both file uploads and manual URL entries
- Implemented server-sent events for real-time progress updates
- Enhanced frontend logic with Alpine.js for better reactivity
- Improved chart rendering and popup functionality
- Added more robust error handling and validation on both frontend and backend

### Version 3.0
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
- Logging System

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
1. Upload file with URLs or enter URLs manually
2. Specify expected certificate name (optional)
3. Process URLs and retrieve SSL certificate details
4. Display real-time results and logs
5. Download results or view detailed error reports

## Usage
1. Navigate to the `ssl-certificate-checker` folder
2. Double-click the `Run_SSL_Checker.bat` file to start the application
3. Chrome will open automatically to http://localhost:5000
4. Choose between file upload or manual URL entry:
   - For file upload: Select a file (XLS, XLSX, or CSV) with URLs
   - For manual entry: Enter URLs in the provided text area (up to 1000 URLs)
5. Enter expected certificate name (optional)
6. Click "Submit"
7. Monitor progress bar and log updates
8. View results table
9. Use "View All Errors" for comprehensive error list (if more than 5 errors)
10. View logs by clicking the "View Logs" button
11. Customize experience (dark mode, font size)
12. Close Chrome to automatically stop the server and close the batch file

[Include the rest of the sections from the original README, updating any parts that might have changed due to the new features]

## License
This project is licensed under the MIT License - see the [LICENSE](app/LICENSE) file for details.

## Contact
For support, feature requests, or any queries, please contact:
- Project Maintainer: Jyothiswaroop Boggavarapu
- Email: bjyothiswaroop7@gmail.com
- GitHub Issues: https://github.com/Jyothiswaroop11/ssl-certificate-checker/issues

We appreciate your feedback to make this tool better!
