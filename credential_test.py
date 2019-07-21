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

    def test_save_credentials(self):
        """
        Test to check whether app saves account credentials
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        """
        Test for saving multiple credentials
        """
        self.new_credentials.save_credentials()
        test_credentials = credentials("jameskirwa34","Kirwa","vamphyllove")
        test_credentials.save_credentials()
        self.assertEqual(len(credentials.credentials_list),2)


    