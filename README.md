# Automated College Outing Approval System

## About

The **Automated College Outing Approval System** is designed to streamline the process of managing and approving outing requests within a college environment. By automating the approval workflow, this system reduces paperwork, enhances communication between students and administration, and ensures a transparent tracking mechanism for all outing activities.

## Features

- **User Authentication**: Secure login system for students and administrative staff.
- **Outing Request Form**: Digital form for students to submit outing requests.
- **Automated Approval Workflow**: Systematic routing of requests to designated approvers.
- **Email Notifications**: Automated alerts to inform users about request statuses.
- **Dashboard Overview**: Administrative panel to monitor and manage outing requests.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/GanesshMM/Automated-College-Outing-Approval-System.git
   cd Automated-College-Outing-Approval-System
   ```

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application requires specific configurations, especially for email notifications. Ensure you set up the following environment variables or update the configuration file accordingly:

- **Email Settings**:

  - `MAIL_SERVER`: SMTP server address (e.g., `smtp.gmail.com`)
  - `MAIL_PORT`: SMTP server port (e.g., `587` for TLS)
  - `MAIL_USE_TLS`: Enable TLS (set to `True` or `False`)
  - `MAIL_USERNAME`: Your email address
  - `MAIL_PASSWORD`: App-specific password or your email password

  **Note**: For Gmail users, it's recommended to use an app-specific password or enable "Less secure app access" for the sender email account.

- **Database Settings**:

  - `DATABASE_URI`: The URI for your database (e.g., `sqlite:///site.db` for a local SQLite database)

These configurations can be set in a `.env` file or directly within your application's configuration settings.

## Usage

1. **Run the Application**:

   ```bash
   python app.py
   ```

2. **Access the Application**:

   Open your web browser and navigate to `http://127.0.0.1:5000/` to start using the system.

## Folder Structure

```
Automated-College-Outing-Approval-System/
├── static/
│   └── ...         # Static files (CSS, JavaScript, images)
├── templates/
│   └── ...         # HTML templates
├── app.py          # Main application script
├── database.py     # Database models and setup
├── mail.py         # Email handling module
├── requirements.txt# Python dependencies
└── README.md       # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

By following this guide, you should be able to set up and run the Automated College Outing Approval System seamlessly. If you encounter any issues or have questions, feel free to open an issue in the repository.
