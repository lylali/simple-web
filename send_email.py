import smtplib

SENDER = 'dinglan.li.ldl@gmail.com'
RECIPIENT = 'lyla.li.ldl@gmail.com'
KEY = 'knyztkzgqfbflxjh'

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
            connection.login(user=SENDER, password=KEY)
            connection.sendmail(from_addr=SENDER, to_addrs=RECIPIENT, msg=self.message)