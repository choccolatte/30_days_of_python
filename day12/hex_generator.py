# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string

def list_of_hexa_colors():
    letters = string.ascii_lowercase[:6]
    nums = str(string.digits)

    hex = letters + nums

    rand_hex = "".join(random.choices(hex, k = 6)) # ['a', '3', 'f', '9', '1', '2']  (A list of 6 items) - "a3f912" (Glued into one string)

    return f'#{rand_hex}' 

print(list_of_hexa_colors())