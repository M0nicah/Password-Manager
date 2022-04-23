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
        test_save_contact test case to test if the user object is saved into the user_details list
       """
       self.new_user.save_user()  # saving the new contact
       self.assertEqual(len(User.user_details), 1)

if __name__ == '__main__':
    unittest.main()


