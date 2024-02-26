class Email():
    def __init__(self, email_address: str, subject_line: str, email_content: str) -> None:
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

inbox = []

def populate_inbox():
    """creates an email object with email address, subject line, and contents, and stores it in inbox."""
    pass

def list_emails():
    """loops through inbox and prints each email’s subject_line, along with a corresponding number."""
    pass