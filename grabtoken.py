import gkeepapi
import getpass
import keyring

def login_grabtoken():
    keep = gkeepapi.Keep()
    username = input('Enter user name :\n')
    try:
        password = getpass.getpass('Enter login/app password: ')
        # google authentication
        keep.login(username, password)
    except gkeepapi.exception.LoginException:
        print('Incorret login credentials')
    except:
        print('If login password throws an error, Enter your App Password.\nRefer to readme on how to obtain your app password')
    finally:
        # save session token
        token = keep.getMasterToken()
        # save username
        with open('username.cred', 'w') as user_cred:
            user_cred.write(username)
        # save master token using keyring
        keyring.set_password('google-keep-token', username, token)
        return keep 