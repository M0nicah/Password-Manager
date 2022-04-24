#!/usr/bin/env python3.10

from passmanager import User, Credentials


def create_new_user(username, user_password):
    """
    Function to create a new user account
    """
    new_user = User(username, user_password)
    return new_user


def save_user(user):
    """
    Function to save a user
    """
    user.save_user()


def user_login(username, user_password):
    """
    a function that checks if the users already exist and allows them to login
    """
    user_confirmed = Credentials.confirm_user(username, user_password)
    return user_confirmed


def delete_user(user):
    """
    Function to delete a user
    """
    user.delete_user()


def display_user(user):
    """
    Function that returns all the saved users
    """
    return user.display_user()


def confirm_user():
    """
    function that verifies that a user with the username entered exists
    """
    return confirm_user()


def create_new_credentials(appName, userName, passWord):
    new_credential = Credentials.create_new_credential(appName, userName, passWord)
    return new_credential


def save_app_credentials(credentials):
    credentials.save_credentials()


def display_credentials(credentials):
    return credentials.display_credentials()


def delete_credentials(credentials):
    credentials.delete_credentials()


def credential_presence(appName):
    return Credentials.check_credential_presence(appName)


def find_credential(appName):
    return Credentials.find_credential(appName)


def generate_new_password(self):
    new_password = Credentials.generate_new_password(self)
    return new_password


def passmanager():
    print("Welcome to Password Manager!")
    print("")
    print(" * " * 20)
    print("  Create an account: ")
    print(" * " * 20)
    print("")
    username = input("Enter username: ")
    user_password = str(input("Enter password: "))
    save_user(create_new_user(username, user_password))
    print("")
    print(" * " * 30)
    print(f"  Hello {username}, your account was created successfully! Your account password is {user_password}")

    print(" * " * 30)
    print(" ")

    while True:
        print("""
        1. Create new Credential
        2. View my Credentials
        3. Delete old Credentials
        4. Find a Credential
        5. Generate a new password
        q. Quit application

        """)
        print("What would you like to do?")
        command = input("")

        if command == "1":
            print("Add new app account details")
            appName = str(input("Enter name of website/app: "))
            userName = str(input("Enter the username you used: "))
            passWord = ""
            print("1.Add my own password")
            print("2.Generate new password")
            password_response = input("")
            if password_response == "1":
                passWord = input("Enter password for the software: ")
                print("")
            elif password_response == "2":
                passWord = generate_new_password(passWord)
                print("")
            else:
                print("Please enter a valid response")

            new = Credentials(appName, userName, passWord)
            new.save_app_credentials()
        elif command == "2":
            credentials_list = Credentials.display_credentials()
            for Credential in credentials_list:
                print(f"Appname: {Credential.appName}")
                print(f"UserName: {Credential.userName}")
                print(f"passWord: {Credential.passWord}")
            if len(credentials_list) == 1:
                print(f"You have {len(credentials_list)} account credential saved")
                print("")
            elif len(credentials_list) > 1:
                print(f"You have {len(credentials_list)} accounts credentials saved")
            else:
                print(f"There are no account credentials saved at the moment")

        elif command == "3":
            appName = input("Enter the name of the website you want to delete: ")
            Credentials.delete_credentials(appName)
            print(f"The credential with name {appName} has been deleted successfully.")

        elif command == "4":
            appName = input("What credential do you want to find? ")
            Credential = Credentials.find_credential(appName)
            print(" * " * 10)
            print(f"Appname: {Credential.appName}")
            print(f"UserName: {Credential.userName}")
            print(f"passWord: {Credential.passWord}")
            print(" * " * 10)

        elif command == "5":
            import random
            import string

            LETTERS = string.ascii_letters
            NUMS = "0123456789"
            SPE = '*&^%$+-_!'
            SYMBOLS = LETTERS + NUMS + SPE
            prompt = int(input("Enter password length: "))
            password = "".join(random.sample(SYMBOLS, prompt))
            print("\n Password Generated successfully!")
            print("")
            print("Your new password is " + str(password))
            print("")

        elif command == "q":
            exit()


if __name__ == '__main__':
    passmanager()
