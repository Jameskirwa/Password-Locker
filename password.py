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

     def __init__(self,account_name,username,password):
        """
        Function to initialize credential fields correctly
        """

        self.account_name = account_name
        self.username = username
        self.password = password


     def save_credentials(self):
        """
        Function to save credentials
        """
        credentials.credentials_list.append(self) 

     @classmethod
     def find_by_name(cls,name):
        """
        cls refers to the entire class
        find_by_name loops through names to check for the name passed if true it returns the name
        introduction of decorator for simple modification
        method that takes a name of an account and returns the account object
        """
        for account in cls.credentials_list:
            if account.account_name == name:
                return account 

     @classmethod
     def generate_password(stringLength = 12):
        """
        Function to generate password
        """
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        size = 10
        return ''.join(random.choice(chars) for x in range(size,18))

     @classmethod
     def display_credentials(cls):
        """
        Function to display accounts and their credentials
        """
        return cls.credentials_list
     def delete_credentials(self):
        """
        Function to delete account credentials
        """
        credentials.credentials_list.remove(self)   
           

          

      


     




    
