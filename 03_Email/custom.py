from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

try:
    host = "smtp.gmail.com"
    port = 587
    username = "" #modify
    password = "" #modify

    from_email = username
    to_list = [""] #modify

    # creating connection and assiginin it to 'SMTP' obj:
    SMTP = smtplib.SMTP(host, port)
    # sayying helllo to server is a MUST!
    SMTP.ehlo()
    # starting the encryption:
    SMTP.starttls()
    # login to server with credentials:
    SMTP.login(username, password)

    # forming the message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Lernen Sie neue Wörter mit uns!"
    message["From"] = "deutschlehrer@at.com"
    # when we don't specify the following line (we don't here yet due to the fact that we want to send to a set of users - but I guess this issue will be solved further in course) it leaves the 'to' section empty!
    #message["To"] = "deutschlehrer@at.com"
    plain_text = "Testen der Nachricht"
    html_text = """\
    <html>
      <head></head>
      <body>
        <p>Hey!<br>
          Testen dieser Emailnachricht. Hergestellt von <a href="https://www.google.com">DeutschLehrer-Team</a>.
        </p>
      </body>
    </html>
    """
    # getting formatted the texts:
    part_1 = MIMEText(plain_text, "plain")
    part_2 = MIMEText(html_text, "html")
    # adding formatted texts to the message to be sent
    message.attach(part_1)
    message.attach(part_2)
    # and finally sending the created message:
    SMTP.sendmail(from_email, to_list, message.as_string())
    # quitting the connection
    SMTP.quit()
    
except smtplib.SMTPException:
    print("Ein Fehler ist aufgetreten!")