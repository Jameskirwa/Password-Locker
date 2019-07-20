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

        # instance variables that take (firstname,lastname & password)
    def save_user(self):
        """
        Function to save user login details
        """
        user.user_list.append(self)    

     




    
