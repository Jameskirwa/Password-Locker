import string
import random
class user:
    """
    Class to define login details for the user in the application
    """
    user_list = []

    def __init__(self,first_name,last_name,password):
        """
        Function to initialize user fields correctly
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        """
        self is a var that reps the instance of an object itself
        instance variables that take (firstname,lastname & password)
        """
    def save_user(self):
        """
        Function to save user login details
        """
        user.user_list.append(self) 

class credentials:
     """
    Class to define credentials for the different accounts
    """
     credentials_list = []


     




    
