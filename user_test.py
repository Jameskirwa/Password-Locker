import unittest
from password import user

class TestUser(unittest.TestCase):
    """
    Class for testing the behaviour of the user class
    """

    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_user = user("James","Kirwa","Uppercase95")

    def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Kirwa")
        self.assertEqual(self.new_user.password,"Uppercase95")    