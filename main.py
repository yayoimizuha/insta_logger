from instaloader import Instaloader, Profile
from os import environ
from requests import get
from pprint import pprint

user_list = \
    get('https://raw.githubusercontent.com/yayoimizuha/youtube-viewcount-logger-python/master/instagram_user.list'). \
        text.split('\n')
user_list = [i for i in user_list if '#' not in i]
pprint(user_list)

instance = Instaloader()

instance.login(environ['user_id'], environ['passwd'])

for i in user_list:
    print(i, Profile.from_username(instance.context, i).followers)
    # input()
