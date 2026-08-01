# Day 12 - Modules

# Whar are Modules?
# A module is a file containing a set of codes or a set of functions which can be included to an application. A module could be a file containing a single variable, a function or a big code base.

# Creating a Module
# To create a module we write our codes in a python script and we save it as a .py file. Create a file named mymodule.py here.

# mymodule.py
def generate_full_name(f_name, l_name):
    return f_name + ' ' + l_name

# Create main.py file in our project and import mymodule.py file.


# Importing a Module
# To import the file we use the import keyword, and the name of the module/file only.
# main.py file
import mymodule
print(mymodule.generate_full_name('Kush', 'Sin')) # Kush # Sin


# Import Functions from a Module
# We can have many functions in a file and we can import all the functions differently.

# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Kush', 'Sin'))
print(sum_two_nums(1, 9))
mass = 100
weight = mass * gravity
print(weight)
print(person)
print(person['firstname'])


# Import Functions from a Module and Renaming
# During importing we can rename the name of the module.

# main.py file
from mymodule import generate_full_name as full_name, person as p, gravity as g, sum_two_nums as total
print(full_name('Kush', 'Sin'))
print(total)
mass = 100
gravity = mass * g
print(weight)
print(p)
print(p['firstname'])


# Import Built-in Modules
# Like other programming languages, we can also import modules by importing the file/function using the key word import. Lets import the common module we will use most of the time. 
# Some of the common built-in modules are - math, datetime, random, os, sys, statistics, collections, json, re, etc.


# OS Module
# Using Python, os module it is possible to automatically perform many operating system tasks. The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.

# import the module
import os
# creating a directory
os.mkdir('directory_name')
# changing teh current directory
os.chdir('path')
# getting current working directory
os.getcwd()
# removing directory
os.mkdir()


# sys module
# the sys module provides functions and variables used to manipulate different parts of the Python runtime environment. FUnction sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is the argument passed from the command line.

# example of a script.py file -
import sys
# print(sys.argv[0], argv[1], sys.argv[2]) # this line would print out: filename argument 1 argument 2
print('Welcome {}, Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))

# Now, to check how this script works we wrote in the command line -
# python script.py Kush 30DaysOfPython

# The result
# Welcome Kush. Enjoy 30DaysOfPython

# Some useful sys commands
# to exit sys
sys.exit()
# to know the largest integer variable it takes
sys.maxsize
# to know the environment path
sys.path
# to know the version of python you are using
sys.version


# Statistics Module
# The statistics module provides functins for mathematical statistics of numeric data. The popular statistical functions which are defined in this module: mean, median, mode, stdev etc.

# example
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean[ages])
print(median[ages])
print(mode[ages])
print(stdev(ages))


# Math module
# Module containing many mathematical operations and constants.

# example
import math as m
print(m.pi) # 3.1451, PI constant
print(m.sqrt(2)) # 1.414, square root 
print(m.pow(2, 3)) # 8.0, exponential function
print(m.floor(9.81)) # 9, rounding to the lowest
print(m.ceil(9.81)) # 10, rounding to the highest
print(m.log10(100)) # 2, logarithm with 10 as base

# Now, we have imported the math module which contains lots of function the module has got, we can use help(math), or dir(math). THis will display the available functions in the module. if we want to import only a specific function from the module we import it as follows -

from math import pi
print(pi)

# It is also possible to import multiple functions at once -
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)
print(sqrt(12))
print(pow(5))
print(floor(9.81))
print(ceil(9.81))
print(math.log10(100))

# But if we want to import all the functions in math module, we can use * .
from math import *
print(pi)
print(sqrt(12))
print(pow(5))
print(floor(9.81))
print(ceil(9.81))
print(math.log10(100))

# Also, whwn we want to import, we can also rename the name of the functions we are importing to something that is easier to remember and use. it
from math import pi as PI
print(PI)



# String module
# a string module is a useful module for many purposes. The example below shows some use of the string module.

import string
print(string.ascii_letters) # a to z, A TO Z
print(string.digits) # 0 - 9
print(string.punctuation) # all special chars



# Random Module
# By now, we are familiar with importing modules. Let us do one more import to get very familiar with it. Let us impport random module which gives us a random numbers between 0 and 0.9999. The random module has lots of functions but in this section, we will only use random and randint.

from random import random, randint
print(random()) # returns a value between 0 - 0.9999, doenst take any arguments
print(randint(5, 100)) # returns a random integer value between 5 and 100. both are inclusive.


# 💻 Exercises: Day 12

# Exercises: Level 1
# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id()) 
#   '1ee33d'
def rand_user_id(name):
    name = name.lower()
    nums = randint(10, 99)
    alpha = string.ascii_lowercase
    single_digit = alpha[:3]

    user_id = name + nums + single_digit
    return user_id
print(rand_user_id('leo'))

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
def user_id_gen_by_user():
    username_len = int(input('Enter username length: '))
    nums_generated = int(input('Enter number of usernames to be generated: '))

    pool = string.ascii_letters + string.digits

    for i in range(username_len):
        username = "".join(random.choice(pool, k = username_len))

    return username 
    

    # times_generated = 0
    # while times_generated <= nums_generated:
    #     generated_username = name + str(nums)
    #     times_generated += 1
    # return generated_username





# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rtrn_seq = f'rgb{r}, {g}, {b}'
    return rtrn_seq
print(rgb_color_gen())


# Exercises: Level 2
# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors():


# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
