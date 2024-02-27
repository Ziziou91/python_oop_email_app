from utility_functions import color, print_line

class Email():
    """Class copies the basic functionality expected from an email."""
    def __init__(self, email_address: str, subject_line: str, email_content: str) -> None:
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    has_been_read = False

    def mark_as_read(self):
        """Sets has_been_read to True when called."""
        self.has_been_read = True

inbox = []

def populate_inbox() -> None:
    """creates an email object with email address, subject line, and contents, and stores it in inbox."""
    initial_emails_data = [
        ["hello@pythontips.com", "British or American english variable names?", "Hi there, one of the most common questions we get asked is best practice for variable spelling and grammar. Check out our website for our editors thoughts on the matter."],
        ["coffee@coderscoffee.yum", "5 roasts for the the coffee-powered coder in your life", "Our head roaster has complied a list of the best brews for programmers passionate about java (coffee)."],
        ["noreply@betterui.com", "Create UI for international audiences", "It's natural to use or experience and intuition to approach great UI, but how do we ensure designs make sense to international audiences. We discussed this concept the worlds leading UI experts."]
        ]
    inbox.extend([Email(*initial_email_data) for initial_email_data in initial_emails_data])

def list_emails() -> None:
    """loops through inbox and prints each email’s subject_line, along with a corresponding number."""
    print("inbox")
    for index, email in enumerate(inbox):
        print(f"{index}\t{email.subject_line}")

def read_email() -> None:
    """Takes a user input (inbox index), then displays selected email and sets has_been_read to True."""
    print(f"{'-'*30}{color.bold}Read email{color.end}{'-'*31}")
    # Validate user input - ensure it can be cast as integer.
    while True:
        try:
            selected_index = int(input("Please select which email you would like to read: "))
        except ValueError:
            print(f"{'-'*10}ERROR! Input must be integer. Please try again.")
            continue
        else:
            break
    print(f"From: {inbox[selected_index].email_address}")
    print(f"Subject: {inbox[selected_index].subject_line}")
    print(f"Content: {inbox[selected_index].email_content}")


if __name__ == "__main__":
    print_line()
    print(f"{'*'*30}{color.bold}email.py{color.end}{'*'*31}")
    print_line()

    populate_inbox()
    print("""The following commands are available:
          \t* list - list all emails in the inbox
          \t* read - read an email in the inbox 
          """)
    menu_choice = input("Enter your input: ")
    # TODO - make sure the user input is valid
    if menu_choice == "list":
        list_emails()
    elif menu_choice == "read":
        read_email()

    print_line()
    print(f"{'*'*29}{color.bold}email.py END{color.end}{'*'*29}")
    print_line()