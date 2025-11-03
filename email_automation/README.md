# 📧 Email Automation Script

A simple yet powerful **Python automation tool** that sends emails automatically with reports, messages, or updates using `smtplib` and `logging`.  
Perfect for automating daily/weekly status emails, project reports, or notifications.

---

## 🚀 Project Goal

To automate the process of sending summary emails using Python — without manual effort.  
This mini project helps you understand:
- SMTP communication
- Python email handling
- Logging and error tracking
- Scheduling and automation basics

---

## 🧱 Project Structure

email_automation/
│
├── main.py # Main script to send emails
├── config/
│ └── email_config.json # Contains sender, receiver, subject, and message info
├── utils/
│ └── email_utils.py # Utility functions for message formatting, attachments
├── logs/
│ └── email_automation.log # Log file for success/error tracking
├── requirements.txt # Required Python libraries
└── README.md # Project documentation


---

## ⚙️ Features

✅ Send emails automatically using Gmail’s SMTP  
✅ Support for plain text or HTML email body  
✅ Centralized logging for success and errors  
✅ Easy configuration through JSON or environment variables  
✅ Extendable to attach files or schedule sending  

---

## 🧩 Tech Stack

| Component | Purpose |
|------------|----------|
| **Python** | Main programming language |
| **smtplib** | For connecting and sending mails |
| **email.mime** | For message structure |
| **logging** | For tracking success and errors |
| **schedule** *(optional)* | For daily or timed automation |

---

## 🪜 How to Run

1️⃣ **Clone the repository**
```bash
git clone https://github.com/Srikanth8036/mini_projects.git
cd mini_projects/email_automation
2️⃣ Create and activate virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate   # On Windows


3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Add your email credentials in config/email_config.json

{
  "sender_email": "your_email@gmail.com",
  "app_password": "your_app_password",
  "receiver_email": "receiver@gmail.com",
  "subject": "Daily Report",
  "message": "Hello, this is an automated email."
}


5️⃣ Run the script

python main.py


6️⃣ Check the logs
Logs will be available inside logs/email_automation.log

🧠 Example Output
Connecting to SMTP server...
Email sent successfully!


Logs:

2025-10-11 10:05:02 - INFO - Email sent successfully.

🧩 Future Enhancements

Add file attachments (PDF, CSV reports)

Integrate with scheduler (e.g., schedule or cron)

Add HTML email templates

Use OAuth2 for secure login instead of app password
