"""
sending emails via python
currently does not work because of policy restrictions
"""

import smtplib


my_email = "pickled.sprout.bay@gmail.com"
password = "Googlebox1"
connection = smtplib.SMTP("smtp.gmail.com") 
connection.starttls() #make connection secure
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="s.schultchen@gmx.com", msg="Hello, I am writing an email using only python")
connection.close

