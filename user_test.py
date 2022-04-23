import unittest
from user import User


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
        self.assertEqual(len(User.user_details), 1)

    def tearDown(self) -> None:
        """
        tearDown method that does clean up after each test case has run.
        """

        User.user_details = []

    def test_save_numerous_user(self):
        """
        test_save_numerous_user to check if we can save multiple users
        objects to our user_details
        """
        self.new_user.save_user()
        test_user = User("tester", "@tester")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_details), 2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from the user details list
        """
        self.new_user.save_user()
        test_user = User("Test", "@tester")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_details), 1)


if __name__ == '__main__':
    unittest.main()

# new_user = User("tester", "@tester")

# print(new_user.username)
