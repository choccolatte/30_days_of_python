from random import *
import string

def rand_user_id():
    name = input('Enter name for the username: ')
    short_name = name[:3].lower()
    num = randint(10, 99)
    rand_dig = choice(string.ascii_letters).lower()
    # name = name.lower() 

    user_id = short_name + str(num) + rand_dig
    return user_id
print(rand_user_id())