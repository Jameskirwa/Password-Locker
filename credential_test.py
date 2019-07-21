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


    def tearDown(self):
        """
        Method that cleans up after each test
        """
        credentials.credentials_list = []

    def test_init(self):
        """
        Test for correct initialization
        """
        self.assertEqual(self.new_credentials.account_name,"Github")
        self.assertEqual(self.new_credentials.username,"Jameskirwa")
        self.assertEqual(self.new_credentials.password,"Uppercase95")

    