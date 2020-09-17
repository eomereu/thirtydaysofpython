import datetime

class MessageUser():
    user_details = []
    messages = []
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
            for detail in self.user_details:
                message = self.base_message.format(
                    name = detail["name"].capitalize(),
                    amount = "%.2f" %(detail["amount"]),
                    date = self.reformat_date(detail["date"])
                )
                self.messages.append(message)
            return self.messages
        return []

    def reformat_date(self, date):
        # Reformats date as dd/mm/yyyy
        return date.strftime('%d/%m/%Y')

# Main function
if __name__ == '__main__':

    obj = MessageUser()
    obj.add_user_detail("Justin", 123.32)
    obj.add_user_detail("john", 94.23)
    obj.add_user_detail("Emilee", 124.32)
    obj.add_user_detail("Jim", 323.4)
    obj.add_user_detail("Ron", 23)
    obj.add_user_detail("sandra", 322.122323)
    obj.add_user_detail("veronica", 32.4)
    obj.add_user_detail("whiTNEY", 99.99)

    #print(obj.get_user_details)

    for i in obj.make_messages():
        print(i, end="\n--------\n\n")