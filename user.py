class User:
    user_details = []  # empty user details

    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password

    def save_user(self):
        """
        save_contact method saves user objects into contact_list
        """
        User.user_details.append(self)

    def delete_user(self):
        User.user_details.append(self)

