import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}!

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was €{amount}.
Have a great one!

Team CFE"""

    def add_user_detail(self, name, amount, email=None):
        detail = {
            "name" : name,
            "amount": amount
        }
        detail["date"] = datetime.datetime.today()
        if email is not None:
            detail["email"] = email
        self.user_details.append(detail)

    @property
    def get_user_details(self):
        return self.user_details

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_user_details:
                message = self.base_message.format(
                    name = detail["name"].capitalize(),
                    amount = "%.2f" %(detail["amount"]),
                    date = self.reformat_date(detail["date"])
                )
                user_email = detail.get("email")
                # to prevent further errors if the user has no email, we filter the ones with email and add them to 'email_messages' list:
                if user_email:
                    user_data = {
                        "email": user_email,
                        "message": message
                    }
                    self.email_messages.append(user_data)
                else: #if the user doesn't have email, add his message to 'messages' list:
                    self.messages.append(message)
            return self.messages #actually redundant in this version
        return [] #actually redundant in this version

    def reformat_date(self, date):
        # Reformats date as dd/mm/yyyy
        return date.strftime('%d/%m/%Y')

    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail["email"]
                user_message = detail["message"]
                try:
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
                    message["Subject"] = "Billing Update!"
                    message["From"] = from_email
                    message["To"] = user_email
                    # getting formatted the texts:
                    part_1 = MIMEText(user_message, "plain")
                    #part_2 = MIMEText(html_text, "html")
                    # adding formatted texts to the message to be sent
                    message.attach(part_1)
                    #message.attach(part_2)
                    # and finally sending the created message:
                    SMTP.sendmail(from_email, [user_email], message.as_string())
                    # quitting the connection
                    SMTP.quit()
                except smtplib.SMTPException:
                    print("Ein Fehler ist aufgetreten!")
            return True
        return False

# Main function
if __name__ == '__main__':

    host = "smtp.gmail.com"
    port = 587
    username = "" #modify
    password = "" #modify

    from_email = username
    #to_list = [""] #modify

    obj = MessageUser()
    obj.add_user_detail("Justin", 123.32, "") #modify
    obj.add_user_detail("john", 94.23, "") #modify
    #obj.add_user_detail("Emilee", 124.32)
    #obj.add_user_detail("Jim", 323.4)
    #obj.add_user_detail("Ron", 23)
    #obj.add_user_detail("sandra", 322.122323)
    #obj.add_user_detail("veronica", 32.4)
    #obj.add_user_detail("whiTNEY", 99.99)

    obj.send_email()

    #for i in obj.make_messages():
    #    print(i, end="\n--------\n\n")