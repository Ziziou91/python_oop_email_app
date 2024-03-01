# OOP Python Email App

OOP Python application designed to simulate a simple email browser. User can view unread emails, read an email, mark as spam and delete emails.

Application is built with vanilla Python and uses CLI to interact with user. Stdout formatting has improved on previous projects - print messages are laid out in a table for improved readability. Table supports multi-line rows, making it well-suited for longer strings of text, such as the body of an email.

## How to install and run the project

### Installation

This application requires `python3` to run. The following command will check if it's installed:

    python3 --version

Output should look something like `Python 3.8.4`. If not you have a couple of options:

1) Install using homebrew. If homebrew is already installed this is as simple as running `brew install`

2) Install using the official installer. You can find your required version at Python.org

### Testing

This app relies on [pytest](https://docs.pytest.org/en/stable/) for testing functionality. In the apps root directory type:

    pytest

You can check if pytest is installed with:

    pytest --version

If this command fails, you might need to install pytest using:

    pip install -U pytest

More details about pip (python package installer) can be found [here](https://pypi.org/project/pip/)

### Running the app

Start with the following command in the apps root directory:

    python3 email.py

You can then interact with the application by using the following commands:

    read x - read an email in the inbox 
    spam x - mark an email as spam
    del x - delete an email
    unread - view unread emails
    help - shows this menu
    quit - quit application

where 'x' is the email number in the inbox table.

## Credits

Code for this application was created by me. Thanks to [Hyperiondev](https://www.hyperiondev.com/) for the project suggestion.

## License

Project is covered by GPL License. Please feel free to modify and use this application.

Thanks for checking out my app! 
