import gkeepapi
import getpass
import keyring


username = input('Enter user name :/n')
print('(If login password throws an error, Enter your App Password.\nRefer to readme on how to obtain your app password')
password = getpass.getpass('Enter login/app password: ')


# google authentication
keep = gkeepapi.Keep()
keep.login(username, password)


# save session token
token = keep.getMasterToken()
keyring.set_password('google-keep-token', username, token)
