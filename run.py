from password import user
from password import credentials

def create_login(firstname,lastname,password):
    """
    Function to create a new login
    """
    new_user = user(firstname,lastname,password)
    return new_user