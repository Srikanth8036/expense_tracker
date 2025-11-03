import schedule
import time
from utils.email_utils import Email_Automation
from datetime import datetime

# def task_scheduler():
#     print('sending a mail for every 10 sec....')
#     schedule.every().seconds.do(Email_Automation().send_email)

#     while True:
#         schedule.run_pending()
#         time.sleep(2)



def task_scheduler():
    if datetime.now().day == 1 and datetime.now().hour == 10:
        print('sending a mail for every 1st day of month at 10 AM....')
        schedule.every().month.at('10:00').do(Email_Automation().send_email)
       
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute