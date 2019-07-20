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