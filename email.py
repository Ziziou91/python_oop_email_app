import sys
from utility_functions import Color, create_char_line, create_table_row, create_title

class Email():
    """Class provides the basic functionality expected for an email."""
    def __init__(self, email_address: str, subject_line: str, email_content: str) -> None:
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    has_been_read = False
    is_spam = False

    def mark_as_read(self):
        """Sets has_been_read to True when called."""
        self.has_been_read = True

    def read_email(self):
        """Prints emails details in terminal and sets has_been_read to True."""
        print(create_char_line())
        print(create_table_row("From:", self.email_address))
        print(create_char_line())
        print(create_table_row("Subject:", self.subject_line))
        print(create_char_line())
        print(create_table_row("Content:", self.email_content))
        print(create_char_line())

        self.has_been_read = True


# ==============Global Variables============== 
inbox = []
help_string = """\nThe following commands are available:
\t* read x - read an email in the inbox 
\t* spam x - mark an email as spam
\t* del x - delete an email
\t* unread - view unread emails
\t* help - shows this menu
\t* quit - quit application
where 'x' is the email number in the table above. 
"""

# ==============Functions==============
def populate_inbox() -> None:
    """creates an email object with email address, subject line, and contents, and stores it in inbox."""
    initial_emails_data = [
        ["hello@pythontips.com", "British or American english variable names?", "Hi there, one of the most common questions we get asked is best practice for variable spelling and grammar. Check out our website for our editors thoughts on the matter."],
        ["coffee@coderscoffee.yum", "5 roasts for the the coffee-powered coder in your life", "Our head roaster has complied a list of the best brews for programmers passionate about java (coffee)."],
        ["noreply@betterui.com", "Create UI for international audiences", "It's natural to use or experience and intuition to approach great UI, but how do we ensure designs make sense to international audiences. We discussed this concept the worlds leading UI experts."],
        ["newsletter@web.com", "Trends in web development to watch in 2024", "Here's a list of some of the developments in web technologies we are most excited about."],
        ["teststring@py.com", "The perfect test string for create_multi_line_table_row", "Hi there, here is a really long string. It's well suited to helping the developer of this app create create_multi_line_table_row, a function to create table rows matched to the length of the string they are given. This will mean that all text is displayed correctly and in a readable manner. So words aren't cut suddenly - the function will work backwards to the last space and start the next line there. Pretty neat right! I hope you like the functionality - please feel free to share feedback and any potential improvements."]
        ]
    inbox.extend([Email(*initial_email_data) for initial_email_data in initial_emails_data])


def list_emails(draw_unread:bool=False) -> None:
    """loops through inbox and prints each email’s subject_line, along with a corresponding number."""
    if draw_unread:
        print(create_title("unread"))
    else:
        print(create_title("inbox"))
    print(f"{create_char_line()}\n{create_table_row()}\n{create_char_line()}")
    for index, email in enumerate(inbox):
        if draw_unread and email.has_been_read:
            pass
        else:
            print(create_table_row(index, email.subject_line))
            print(create_char_line())


def validate_menu_choice(user_str: str) -> list:
    """Make sure the user input is valid. So:"""
    user_list = user_str.split(" ")
    while True:
        if len(user_list) == 1:
            # Validation for single word inputs ('unread' and 'quit')
            valid_inputs = ["unread", "help", "quit"]
            if user_list[0] in valid_inputs:
                break
        elif user_list[1].isdigit():
            # Validation for everything else. So:
            # 1) Can be split into a list with length of 2
            # 2) First part of input is in 'valid_inputs'
            # 3) Second part of input corresponds to index of value in 'inbox' 
            valid_inputs = ["read", "spam", "del"]
            inbox_indexes = [i for i, _ in enumerate(inbox)]
            user_list[1] = int(user_list[1])
            if len(user_list) == 2 and user_list[0] in valid_inputs and user_list[1] in inbox_indexes:
                break

        # Print error message and ask user for new input if previous is not valid.
        print(f"\n{'-'*10}ERROR! {user_str} is not a valid input. Please try again.{'-'*10}\n")
        user_str = input("Enter your input: ")
        user_list = user_str.split(" ")

    return user_list


# ==============main() function==============
def main() -> None:
    """populates inbox with sample emails and prints before asking for user input."""
    print(create_char_line())
    print(f"{'*'*36}{Color.bold}email.py{Color.end}{'*'*35}")
    print(create_char_line())

    # Create 4 instances of Email class for user to interact with.
    populate_inbox()

    list_emails()
    print(help_string)
    while True:
        # Get user input and prepare for command logic.
        menu_choice = input("Enter your input: ")
        validated_input = validate_menu_choice(menu_choice)
        if len(validated_input) == 2:
            email = validated_input[1]
        command = validated_input[0]

        # Route with command variable and execute desired logic.
        if command == "read":
            print(create_title(f"email {email}"))
            inbox[email].read_email()
            print("\n\thelp - list all available commands\n")
        elif command == "spam":
            inbox[email].is_spam = True
            print(f"\nemail {email} has been marked as spam")
        elif command == "del":
            del inbox[email]
            print("Email deleted")
            list_emails()
        elif command == "unread":
            list_emails(True)
            print("\n\thelp - list all available commands\n")
        elif command == "help":
            print(help_string)
        elif command == "quit":
            print(create_char_line())
            print(f"{'*'*33}{Color.bold}email.py END{Color.end}{'*'*34}")
            print(create_char_line())

            sys.exit()

# ==============EXECUTION STARTS HERE==============
if __name__ == "__main__":
    main()
