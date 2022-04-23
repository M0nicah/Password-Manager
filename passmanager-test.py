import unittest
from passmanager import User, Credentials

users_list = []


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Monica", "@monica")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Monica")  # add assertion here
        self.assertEqual(self.new_user.user_password, "@monica")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user_details list
       """
        self.new_user.save_user()  # saving the new contact
        self.assertEqual(len(User.users_list), 1)


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("Twitter", "m0nica", "@monica123")


def test_in(self):
    self.assertEqual(self.new_credentials.appName, 'Twitter')
    self.assertEqual(self.new_credentials.userName, 'm0nica')
    self.assertEqual(self.new_credentials.passWord, '@monica123')


def tearDown(self) -> None:
    """
    tearDown method that does clean up after each test case has run.
    """
    User.users_list = []


def test_save_app_credentials(self):
    """
    test_save_credential to check if we can save  users app names and passwords
    """
    self.new_credentials.save_app_credentials()
    self.assertEqual(len(Credentials.credentials_list), 1)


def test_delete_credentials(self):
    """
    test_delete_user to test if we can remove a user from the users list
    """
    self.new_credentials.save_app_credentials()
    test_credential = Credentials("Instagram", "pretty", "@pretty123")
    test_credential.save_app_credentials()

    self.new_user.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list), 1)


def test_credential_presence(self):
    """
    test to check if we can return a true or false based on whether we find or can't find the credential.
    """
    self.new_credentials.save_credentials()
    test_credential = Credentials("Instagram", "pretty", "@pretty123")
    test_credential.save_app_credentials()

    found_credential = Credentials.credential_presence("Instagram")
    self.assertTrue(found_credential)


def test_display_credentials(self):
    """
    method that displays all the credentials that has been saved by the user
    """
    self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()

# new_user = User("tester", "@tester")

# print(new_user.username)
