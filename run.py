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


def generate_password():
    """
    Function to create a password automatically
    """
    password = credentials.generate_password()
    return password  

def display_credentials():
    """
    Function to display account and credentials
    """
    return credentials.display_credentials()

def del_account(credential):
    """
    Function that deletes an account
    """
    credential.delete_credentials()    

def main():
    # print("Welcome to password locker :)")
    # print("What\'s your name?")
    # name = input()
    # I then use a series of if-elif-else statements to check user input 
    # and call the functions we have just defined depending on the user's choice.
    while True:

        print(f"Hello.Please use the short codes :li to create your password locker account :ex - To exit the application")
    
        short_code = input().lower()

        if short_code == 'li':

            print('Login')
            print('*'*15)

            print("First name....")
            firstname = input()

            print("Last name....")
            lastname = input()

            print("Password....")
            password = input()

            save_user(create_login(firstname,lastname,password))
            print('\n')
            
            while True:

                print(f"Welcome {firstname}.Use the following commands: ca-Create a new account :da - Display all accounts :dl - Delete an account :lo - Log out ")
                print('\n')
                shorter_code = input().lower()

                if shorter_code == 'ca':
                    print("Save new account credentials")
                    print('^'*12)

                    print('Name of the account.....')
                    accname = input()

                    print('Username.....')
                    username = input()
                    while True:
                        print('Use: \n ep >> To input your password \n gp >> To generate a password')
                        pass_code = input().lower()

                        if pass_code == 'ep':

                            print('Password....')
                            password = input()
                            break

                        elif pass_code == 'gp':
                            password = generate_password()
                            break

                        else:
                            pass

                    save_credential(add_account(accname,username,password))
                    print('\n')
                    print(f"New account \'{accname}\' created")        

                elif shorter_code == 'da':
                    if display_credentials():
                        for credential in display_credentials():
                            print('-' * 18)
                            print(f" Account name >> {credential.account_name}  \n Username >> {credential.username} \n password >> {credential.password}")
                            print('-' * 18)
                            
                elif shorter_code == 'dl':
                    pass

                elif shorter_code == 'lo':
                    print('Thank you for using this app :)')
                    break

                else:
                    print('Sorry :( .The command doesn\'t exist.Try again with :li' )
                    print('-'*8)

        elif short_code == 'ex':
            print("Hope you enjoyed the application.")
            break


        else:
            print('\n')
            print("Sorry :( .The command does not exist.Try again with :li")
            print('-'*8)
            print('\n')

if __name__ == '__main__':
    main()


