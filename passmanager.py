
#         print("Account created Successfully!")
#     elif command == "2":
#         print("Log in")
#     elif command == "3":
#         print(str(input("Website name: ")))
#         print(str(input("Website Password: ")))
#         print("New password saved!")
#     elif command == "4":
#         print("Password deleted successfully")
#     elif command == "5":
#         import random
#         import string
#
#         LETTERS = string.ascii_letters
#         NUMS = "0123456789"
#         SPE = '*&^%$+-_!'
#         SYMBOLS = LETTERS + NUMS + SPE
#         prompt = int(input("Enter password length: "))
#         password = "".join(random.sample(SYMBOLS, prompt))
#         print("\n Password Generated successfully!")
#         print("Your new password is " + str(password))
#     elif command == "q":
#         print("\n Goodbye!")


class User:
    users_list = []  # empty user details

    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password

    def create_new_user(self, username, user_password):
        new_user = User(username, user_password)
        return new_user

    def save_user(self):
        """
         test case to check if the user is added to the user list
        """
        User.users_list.append(self)

    @classmethod
    def delete_user(cls, self):
        User.users_list.remove(self)

    def display_user(self, cls):
        return cls.users_list


class Credentials:
    credentials_list = []

    @classmethod
    def confirm_user(cls, username, user_password):
        users: str = ""
        for user in User.users_list:
            if user.username == username and user.user_password == user_password:
                users == User.username
        return users

    def __init__(self, appName, userName, passWord):
        """
        test case that check if the credentials are initialized properlyy
        """
        self.appName = appName
        self.userName = userName
        self.passWord = passWord

    def create_new_credential(self, appName, userName, passWord):
        new_credential = Credentials(appName, userName, passWord)
        return new_credential

    def save_app_credentials(self):
        """
        test case to add new credentials(password and app names)
        """
        Credentials.credentials_list.append(self)
    @classmethod
    def delete_credentials(cls, appName):

        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        for credential in cls.credentials_list:
            if credential.appName == appName:
                cls.credentials_list.remove(appName)
        # Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, appName):
        """
        Method that takes in an applications name and returns a credential that matches that app
        """
        for credential in cls.credentials_list:
            if credential.appName == appName:
                return credential

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list
        # Credentials.display_credentials()
        # pass

    # def save_credentials(self):
    #     Credentials.save_app_credentials()
    #     pass

    @classmethod
    def check_credential_presence(cls, appName):
        return Credentials.credential_presence(appName)
        pass

    def generate_new_password(self):
        import random
        import string

        LETTERS = string.ascii_letters
        NUMS = "0123456789"
        SPE = '*&^%$+-_!'
        SYMBOLS = LETTERS + NUMS + SPE
        prompt = int(input("Enter password length: "))
        password = "".join(random.sample(SYMBOLS, prompt))
        print("\n Password Generated successfully!")
        print("Your new password is " + str, {password})

    @classmethod
    def credential_presence(cls, param):
        pass
