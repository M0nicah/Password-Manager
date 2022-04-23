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


if __name__ == '__main__':
    unittest.main()
