This is a command line interface (CLI) program that allows users to manage their contacts. Users can add new contacts, view existing contacts, update contacts, and delete contacts.

Getting Started
Prerequisites
Python 3.6 or higher
Pip package manager
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/<username>/<repository-name>.git
Navigate to the project directory:
bash
Copy code
cd <repository-name>
Install the dependencies:
Copy code
pip install -r requirements.txt
Usage
To start the program, run the following command in your terminal:

Copy code
python cli.py
Once the program is running, you can use the following commands:

add: Adds a new contact to the list. The user will be prompted to enter the contact's name, phone number, and email address.
show: Displays a list of all contacts.
update: Updates an existing contact. The user will be prompted to enter the name of the contact to update, as well as the new phone number and email address.
delete: Deletes an existing contact. The user will be prompted to enter the name of the contact to delete.
exit: Exits the program.
Running the tests
This project uses the Pytest library for testing. To run the tests, navigate to the project directory and run the following command:

Copy code
pytest
Built With
Python 3.6
Click - A Python package for creating command line interfaces.
Rich - A Python package for styling console output.
Authors
Your Name - Your GitHub Profile
License
This project is licensed under the MIT License - see the LICENSE file for details.