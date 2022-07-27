import smtplib
import os

BLOG_SENDER_EMAIL = os.getenv('BLOG_SENDER_EMAIL')
BLOG_RECIPIENT = os.getenv('BLOG_RECIPIENT')
BLOG_KEY = os.getenv('BLOG_KEY')

class EmailManager:
    def __init__(self, name, email, phone, message):
        self.message = f"Subject:New message from website.\n\n" \
                       f"Name: {name}\n" \
                       f"Email: {email}\n" \
                       f"Phone Number: {phone}\n" \
                       f"Meaasge: {message}"

    def send_email(self):
        with smtplib.SMTP('smtp.gmail.com', 587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=BLOG_SENDER_EMAIL, password=BLOG_KEY)
            connection.sendmail(from_addr=BLOG_SENDER_EMAIL, to_addrs=BLOG_RECIPIENT, msg=self.message)