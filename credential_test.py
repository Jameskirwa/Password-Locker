import unittest  #importing the unitest module
from password import credentials  #importing the credetial class

class TestCredentials(unittest.TestCase):
    """
    Class to test behaviour of the credentials class
    """
    def setUp(self):
        """
        Setup method that defines instructions
        """
        self.new_credentials = credentials("Github","Jameskirwa","Uppercase95")

    