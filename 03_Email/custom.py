import smtplib

host = "smtp.gmail.com"
port = 587
username = "" #modify
password = "" #modify

from_email = username
to_list = [""] #modify
message = "" #modify

SMTP = smtplib.SMTP(host, port)
SMTP.ehlo()
SMTP.starttls()
SMTP.login(username, password)

SMTP.sendmail(from_email, to_list, message)

SMTP.quit()