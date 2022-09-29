"""
sending emails via python
currently does not work because of policy restrictions
need to use 2 step varification and app password
"""
import os
import smtplib

SENDER_EMAIL = "pickled.sprout.bay@gmail.com"
PASSWORD = os.getenv("email_key")
RECEIVER_EMAIL = "s.schultchen@gmx.com"
TEXT = "Hello, I am writing an email using only python"
SUBJECT = "Python Email"
MESSAGE = f"Subject: {SUBJECT}\n\n{TEXT}"

connection = smtplib.SMTP("smtp.gmail.com")
connection.ehlo()
connection.starttls() #make connection secure (Transport Layer Security)
connection.ehlo()
connection.login(user=SENDER_EMAIL, password=PASSWORD)

connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=MESSAGE)
connection.quit()
