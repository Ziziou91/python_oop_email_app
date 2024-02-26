class Email():
    def __init__(self, email_address: str, subject_line: str, email_content: str) -> None:
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

test = Email("test@test.com", "Hello there!", "Hi there, here is the content of my test email.")

print("email address: ", test.email_address)
print("subject line: ", test.subject_line)
print("email content: ", test.email_content)
