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

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ssl-certificate-checker.git
   cd ssl-certificate-checker
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```
   On Windows, use `set` instead of `export`.

5. Initialize the database (if applicable):
   ```
   flask db upgrade
   ```

6. Run the application:
   ```
   flask run
   ```

7. Open a web browser and navigate to `http://localhost:5000`

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

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
