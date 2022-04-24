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






