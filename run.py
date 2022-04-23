#!/usr/bin/env python3.10

from user import User


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


def display_users():
    """
    Function that returns all the saved users
    """
    return User.display_users()
