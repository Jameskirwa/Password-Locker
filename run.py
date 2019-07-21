from password import user
from password import credentials

def create_login(firstname,lastname,password):
    """
    Function to create a new login
    """
    new_user = user(firstname,lastname,password)
    return new_user

def add_account(accname,username,password):
    """
    Function to add a new account and its credentials
    """
    new_credentials = credentials(accname,username,password)
    return new_credentials

def save_user(user):
    """
    Function to save login details for the user
    """
    user.save_user() 

def save_credential(account):
    """
    Function to save account credentials details
    """
    account.save_credentials()     



