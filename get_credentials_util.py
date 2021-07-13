import json
from glob import glob
def get_credentials(json_file=None):
    try:
        if json_file:
            try:
                credential = glob(json_file)[0]
            except ValueError:
                print("couldn't find specified json at",json_file)
                raise ValueError
        else:
            credential = glob("credentials.json")[0]
        # print('using credentials stored locally at', credential)
        with open(credential, 'r') as cred:
            a = json.load(cred)
        username, password = a['username'], a['password']
        return username, password
    except (IndexError, ValueError):
        username = input("Please enter your username:")
        password = input("Please enter your password:")
        return username, password

