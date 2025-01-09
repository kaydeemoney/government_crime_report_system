# Gvt Online Crime Reporting System

## Overview

The **Online Crime Reporting System** allows users to report fraud or other crimes anonymously or with identifiable information. The system facilitates the submission, tracking, and review of reports by both the users and admins, providing a clear workflow from submission to resolution. This application is built using **Python Flask** with **SQLAlchemy** for database interaction and **MySQL** as the database management system.

---

## Features

- **User Reporting**: Allows users to submit crime reports with or without personal information.
- **Track Report Status**: Users can track their reports using a unique tracking ID.
- **Admin Review Dashboard**: Admins can review submitted reports, add verdicts, and update the report status.
- **Secure Admin Login**: Admins are required to log in with email and password to access the review system.
- **User-Friendly Interface**: Designed with simplicity in mind to allow easy navigation and report submission.

---

## Tech Stack

- **Frontend**: HTML, CSS, Jinja templating
- **Backend**: Python, Flask
- **Database**: MySQL, SQLAlchemy (ORM)
- **Security**: Sessions for admin login
- **UUID**: For generating unique tracking IDs for each report

---

## Getting Started

### Prerequisites

To get this project up and running, you’ll need the following installed:

- Python 3.7 or later
- MySQL Server
- Pip (Python package manager)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/crime-reporting-system.git
    cd crime-reporting-system
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure your **MySQL** database with the necessary tables:

    - Set up the database schema by running the `app/models.py` file to create the necessary tables (`User`, `Report`, `ReportReview`).

4. Set up environment variables:

    - Configure the MySQL database connection and Flask settings by editing the `.env` file with your database credentials.

5. Run the Flask development server:

    ```bash
    flask run
    ```

Now, you can navigate to `http://127.0.0.1:5000/` to start using the application.

---

## Routes

- **`/`**: Home page of the application.
- **`/report`**: Form to submit a new report.
- **`/follow_up`**: Track an existing report by providing a tracking ID.
- **`/admin/login`**: Admin login page for secure access to the admin dashboard.
- **`/admin_dashboard`**: Dashboard for admins to view and manage reports.
- **`/review/<report_id>`**: Page for admins to review a specific report and provide a verdict.

---

## Security

- **Admin Authentication**: Admins are authenticated through an email and password login system. Session management ensures that only logged-in admins can access sensitive data.
- **Data Privacy**: Users can choose to report anonymously, ensuring their data remains confidential.
- **Password Protection**: Passwords are securely handled with proper hashing techniques.

---

## Lessons Learned & Future Improvements

### Lessons Learned

- The importance of **clear code structure** (MVC architecture) in maintaining scalability.
- The **need for robust security measures**, especially when handling sensitive data.
- **Database performance optimizations** will be crucial as the application grows.

### Future Improvements

- Implement **password hashing** for enhanced security.
- Optimize **database queries** for better performance and scalability.
- Improve **user experience** with real-time validation and feedback.
- Implement **unit testing** for comprehensive coverage.

---

## Contributing

We welcome contributions! Please fork the repository, create a new branch, and submit a pull request with your improvements. Ensure your code is well-tested before submitting.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [MySQL](https://www.mysql.com/)
- [UUID](https://docs.python.org/3/library/uuid.html)
