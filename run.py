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


def display_saved_credentials():
    return Credentials.display_credentials()


def delete_credentials(credentials):
    credentials.delete_credentials()


def credential_presence(appName):
    return Credentials.check_credential_presence(appName)


def find_credential(appName):
    return Credentials.find_credential(appName)


def generate_password(self):
    new_password = Credentials.generate_new_password(self)
    return new_password


def passmanager():
    print("Welcome to Password Manager!")
    print("Select a command to continue: ")

    command = True

    while command:  # commands to guide the user
        print("""
        1.Create New Account
        2.Already have an account, Sign me in.
        Q.Exit/Quit
        """)

        print(" * " * 20)

        command = input("What would you like to do? ")

        if command == "1":
            print("Sign Up")
            print("#" * 40)
            username = (input("Enter username: "))
            user_password = ""
            while True:
                print("Do you want to generate a strong password? (y/n)")
                response = input("")
                if response == "y":
                    user_password = generate_password(user_password)
                    break
                elif response == "n":
                    user_password = input("Enter your password: ")
                    break
                else:
                    print("Password is invalid!")

            save_user(create_new_user(username, user_password))
            print(f"Hello {username}, a new account was created successfully! Your account password is {user_password}")

            print("*" * 30)
        elif command == "2":
            print("* Welcome back! Sign In... *")
            print("#" * 30)

            username = input("Enter your username: ")
            user_password = input("Enter password: ")
            user_login(username, user_password)
            while True:
                print("""
                Select command to proceed
                """)


if __name__ == '__main__':
    passmanager()
