import datetime

plain_message = """Hi {name}!

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was €{amount}.
Have a great one!

Team CFE"""

def reformat_date(date):
    # Reformats date as dd/mm/yyyy
    return date.strftime('%d/%m/%Y')

def format_messages(names, amounts):
    messages = []
    today = datetime.datetime.today()
    if len(names) == len(amounts):
        for idx, val in enumerate(names):
            messages.append(plain_message.format(
                name = val.capitalize(),
                date = reformat_date(today),
                amount = "%.2f" %(amounts[idx])
            ))
    else:
        return "Error"
    return messages

# Main function
if __name__ == '__main__':

    names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
    amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

    prepared_messages = format_messages(names, amounts)

    for i in prepared_messages:
        print(i, end="\n--------\n\n")