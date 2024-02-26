# OOP Email App

Simple app to practice utilising OOP design patterns. 

## Upcoming Functionality


* Create an `Email` class and initialise a constructor that takes in three arguments:
    * `email_address` - the email address of the sender.
    * `subject_line` - the subject line of the email.
    * `email_content` - the contents of the email.
* The `Email` class should contain the following class variable and default value:
    * `has_been_read` - initialised to False.
* The `Email` class should also contain the following class method to edit the values of the email objects:
    * mark_as_read which should change has_been_read to True.
* Initialise an empty variable called inbox of type list to store, and access, the email objects.
    * Note: you can have a list of objects.
* Create the following functions to add functionality to your email simulator:
    * `populate_inbox()` - a function which creates an email object with the email address, subject line, and contents, and stores it in the inbox list.
    
        Note: At program start-up, this function should be used to populate your inbox with three sample email objects for further use in your  program. This function does not need to be included as a menu option for the user.
    * `list_emails()` - a function that loops through the inbox and prints each email’s subject_line, along with a corresponding number. For example, if there are three emails in the Inbox:
        0 Welcome to HyperionDev!
        1 Great work on the bootcamp!
        2 Your excellent marks! 
    This function can be used to list the messages when the user chooses to read, mark as spam, and delete an email.
        Tip: Use the enumerate() function for this.
* read_email() - a function that displays a selected email, together with the email_address, subject_line, and email_content, and then  sets its has_been_read instance variable to True.
For this, allow the user to input an index, such that read_email(i)
prints the email stored at position i in the list. Following the example
above, an index of 0 will print the email with the subject line
“Welcome to HyperionDev!”.
* Your task is to build out the class, methods, lists, and functions to get
everything working! Fill in the rest of the logic for what should happen
when the user chooses to:
