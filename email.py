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

def populate_inbox():
    """creates an email object with email address, subject line, and contents, and stores it in inbox."""
    initial_emails_data = [
        ["hello@pythontips.com", "British or American english variable names?", "Hi there, one of the most common questions we get asked is best practice for variable spelling and grammar. Check out our website for our editors thoughts on the matter."],
        ["coffee@coderscoffee.yum", "5 roasts for the the coffee-powered coder in your life", "Our head roaster has complied a list of the best brews for programmers passionate about java (coffee)."],
        ["noreply@betterui.com", "Create UI for international audiences", "It's natural to use or experience and intuition to approach great UI, but how do we ensure designs make sense to international audiences. We discussed this concept the worlds leading UI experts."]
        ]
    inbox.extend([Email(*initial_email_data) for initial_email_data in initial_emails_data])

def list_emails():
    """loops through inbox and prints each email’s subject_line, along with a corresponding number."""
    print("inbox")
    for index, email in enumerate(inbox):
        print(f"{index}\t{email.subject_line}")

if __name__ == "__main__":
    populate_inbox()
    list_emails()