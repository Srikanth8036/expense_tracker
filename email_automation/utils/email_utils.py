# import os 
# import smtplib 
# import getpass

# SMTP_SERVER = "smtp.gmail.com"
# SMPT_PORT = 465
# SENDER = 'srikanthsri8036@gmail.com'
# RECEIVER = SENDER

# subject = 'this is subject'

# body = 'this is body'

# msg = f"Subject: {subject}\n\n{body}"

# PASSWORD = getpass.getpass('enter your 16 digits password:- ')


# try:
#     with smtplib.SMTP_SSL(SMTP_SERVER, SMPT_PORT) as server:
#         server.login(SENDER,PASSWORD)
#         print('logined to server successfully.....')

#         server.sendmail(SENDER, RECEIVER, msg)
#         print('sent the first msg successfully')
# except smtplib.SMTPAuthenticationError:
#     print("❌ Authentication failed. Please check:")
#     print("   1. You are using the correct 16-digit App Password, not your regular password.")
#     print("   2. You entered the correct email address.")
# except Exception as e:
#     print(f"An error occurred: {e}")
    # eciq efde gdku ynyl  CHECK HERE================================================================================

# import smtplib
# import getpass
# import os

# # The new tools for building the email "envelope" and its "parts"
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication

# # --- Configuration (same as before) ---
# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 465
# SENDER_EMAIL = input("Enter your Gmail address: ")
# RECIPIENT_EMAIL = SENDER_EMAIL
# SENDER_PASSWORD = getpass.getpass("Enter your 16-digit Google App Password: ")

# # --- Phase 2: Build the Email Message using the 'email' library ---

# # 1. Create the main "envelope"
# #    'alternative' is important for emails with both text and HTML
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "Project Status Update & Report"
# msg['From'] = SENDER_EMAIL
# msg['To'] = RECIPIENT_EMAIL

# # 2. Create the HTML body of the email
# #    This allows for formatting like bold text, links, etc.
# html_body = """
# <html>
#   <body>
#     <h3>Project Phoenix: Status Update</h3>
#     <p>
#       Hello Team,<br><br>
#       The project is progressing well and we are on schedule. <b>All milestones for this week have been met.</b>
#       <br><br>
#       The latest performance report is attached to this email for your review.
#       <br><br>
#       You can view the project dashboard here: <a href="https://www.google.com">Project Dashboard</a>.
#       <br><br>
#       Best regards,<br>
#       The Automated System
#     </p>
#   </body>
# </html>
# """

# # 3. "Put" the HTML letter into the envelope
# #    We create a MIMEText object and attach it to our main message
# msg.attach(MIMEText(html_body, 'html'))


# # 4. Prepare and attach the file
# filename = "report.txt"
# try:
#     # 'rb' means read in binary mode, which is required for attachments
#     with open(filename, 'rb') as attachment:
#         # Create the attachment part
#         part = MIMEApplication(attachment.read(), _subtype='txt')
    
#     # Add a header to tell the email client this is an attachment
#     part.add_header('Content-Disposition', 'attachment', filename=filename)
    
#     # "Put" the attachment into the envelope
#     msg.attach(part)
#     print(f"✅ Successfully prepared attachment: {filename}")

# except FileNotFoundError:
#     print(f"❌ Error: The file '{filename}' was not found. Please create it.")
#     exit() # Stop the script if the file is missing


# # --- Send the Email (this part is almost identical to Phase 1) ---
# try:
#     with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
#         server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
#         # We must convert the message object to a string before sending
#         server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        
#         print("🚀 Professional email with attachment sent successfully!")

# except Exception as e:
#     print(f"An error occurred: {e}")


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

