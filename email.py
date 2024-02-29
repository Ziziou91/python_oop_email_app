from utility_functions import color, create_char_line, create_table_line, create_title

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

    def read_email(self):
        """Prints emails details in terminal and sets has_been_read to True."""
        print(f"From: {self.email_address}")
        print(f"Subject: {self.subject_line}")
        print(f"Content: {self.email_content}")
        self.has_been_read = True

inbox = []

# ==============Functions==============
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
    print(create_title("inbox"))
    print(f"{create_char_line()}\n{create_table_line()}\n{create_char_line()}")
    for index, email in enumerate(inbox):
        print(create_table_line(index, email.subject_line))
        print(create_char_line())


def validate_menu_choice(user_str: str) -> list:
    """Make sure the user input is valid. So:
    1) Can be split into a list with length of 2
    2) First part of input is in 'valid_inputs'
    3) Second part of input corresponds to index of value in 'inbox' 
    """
    valid_inputs = ["read", "spam", "del"]
    inbox_indexes = [i for i, _ in enumerate(inbox)]
    user_list = user_str.split(" ")
    while True:
        if user_list[1].isdigit():
            user_list[1] = int(user_list[1])
            if len(user_list) == 2 and user_list[0] in valid_inputs and user_list[1] in inbox_indexes:
                break

        # Print error message and ask user for new input if previous is not valid.
        print(f"\n{'-'*10}ERROR! {user_str} is not a valid input. Please try again.\n")
        user_str = input("Enter your input: ")
        user_list = user_str.split(" ")

    return user_list


# ==============main() function==============
def main() -> None:
    """populates inbox with sample emails and prints before asking for user input."""
    print(create_char_line())
    print(f"{'*'*36}{color.bold}email.py{color.end}{'*'*35}")
    print(create_char_line())

    populate_inbox()
    list_emails()

    print("""\nThe following commands are available:
\t* read x - read an email in the inbox 
\t* spam x - mark an email as spam
\t* del x - delete an email
where 'x' is the email number in the table above. 
          """)
    menu_choice = input("Enter your input: ")
    command, email = validate_menu_choice(menu_choice)
    print(f"{command} {email} is a valid input! Great work!")
    if command == "read":
        inbox[email].read_email()
    elif command == "spam":
        print("call spam method")
    elif command == "del":
        print("call delete method")



    print(create_char_line())
    print(f"{'*'*33}{color.bold}email.py END{color.end}{'*'*34}")
    print(create_char_line())


# ==============EXECUTION STARTS HERE==============
if __name__ == "__main__":
    main()
