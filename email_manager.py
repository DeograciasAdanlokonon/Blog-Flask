import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")


class NewEmail:
    def __init__(self):
        self.owner = MY_EMAIL
        self.password = PASSWORD

    def send_email(self, name, phone, email, message):

        body = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.owner, password=self.password)
            connection.sendmail(
                from_addr=self.owner,
                to_addrs=self.owner,
                msg=f"Subject:New message\n\n{body}"
            )


