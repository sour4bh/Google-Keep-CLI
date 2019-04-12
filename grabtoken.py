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
    except:
        print('If login password throws an error, Enter your App Password.\nRefer to readme on how to obtain your app password')
    # save session token
    token = keep.getMasterToken()
    keyring.set_password('google-keep-token', username, token)
    return keep