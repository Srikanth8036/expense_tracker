import smtplib
import os
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import json
import logging 


BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, 'logs', 'email_automation.log')
# Ensure log directory exists before configuring logging
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

class Email_Automation:
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465
    SENDER_EMAIL = 'srikanthsri8036@gmail.com'
    RECIPIENT_EMAIL = SENDER_EMAIL
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(BASE_DIR, 'config', 'email_config.json')


    def send_email(self):
        with open(self.config_path, 'r') as file:
            data = json.load(file)
            
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "A little reminder of how much I love you ❤️"
        msg['From'] = data['sender_email']
        msg['To'] = data['receiver_email']

        html_body = """
<html>
  <body style="font-family: Arial, sans-serif; color: #444; background-color: #fffafc; padding: 20px;">
    <h2 style="color: #d63384;">💖 Hey Soujanya, My Forever Person 💖</h2>
    <p style="font-size: 16px; line-height: 1.6;">
      Just taking a small break from work to tell you something simple — <b>I love you.</b><br><br>
      You make every single day feel lighter, warmer, and more meaningful.<br><br>
      I’ve attached a tiny note with this mail — something from my heart to yours. 💌<br><br>
      Always remember, no matter how busy life gets, you’ll always be my calm in the storm.<br><br>
      Yours, always and forever,<br>
      <b>Srikanth ❤️</b>
    </p>
  </body>
</html>
"""


        # msg.attach(MIMEText(html_body, 'html'))
        msg.attach(MIMEText(html_body.strip(), 'html'))

        file_path = os.path.join(self.BASE_DIR, 'report.txt')

        try:
            with open(file_path, 'rb') as application:
                part = MIMEApplication(application.read(), _subtype='txt')
                
            part.add_header('Content-Disposition', 'attachment', filename=file_path)
            msg.attach(part)
        except FileNotFoundError as e:
            print(f'there is no such file {e}')

        try:
            with smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT) as server:
                # Use password from config (data['password']) or raise a clear error if missing
                password = data.get('password')
                if not password:
                    raise ValueError('No password provided in config (email_config.json)')
                server.login(data['sender_email'], password)
                print('logged into server')

                server.sendmail(data['sender_email'], data['receiver_email'], msg.as_string())
                print('sent mail successfully.... and logged the info')
                logging.info('Email sent successfully.')

        except smtplib.SMTPAuthenticationError as e:
            print(f'auth error {e}')
            logging.error(f'authentication error: {e}')

        except Exception as e:
            print(f'found error is {e}')
            logging.error(f'unexpected error: {e}')


# if __name__ == "__main__":
#     Email_Automation().send_email()

