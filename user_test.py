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

    def test_save_user(self):
        """
        Test to check whether app saves user login details
        """
        self.new_user.save_user()
        self.assertEqual(len(user.user_list),1)
        """
        So by defining the condition if __name__ == '__main__': 
        we are confirming that anything inside the if block should run 
        
        """
if __name__ == '__main__':
    unittest.main()               