# Day 14 - Higher Order Functions

# In python functions are treated as first class citizens, allowing you to perform the following operations on functions:

#   - A function can take one or more functions as parameters
#   - A function can be returned as a result of another function
#   - A function can be modified
#   - A function can be assigned to a variable

# In this section, we will cover
#   1. Handling functions as parameters
#   2. Returning functions as return value from another functions
#   3. Using Python closures and decorators


# Function as a Parameter
def sum_num(nums): #normal function
    return sum(nums) # a sad function abusing the built-in sum function
 
def higher_order_funcs(f, lst): # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_funcs(sum_num, [1, 2, 3, 4, 5])
print(result) # 15


# Function as a Return Value
def square(x): # a square function
    return x ** 2

def cube(x): # a cube function
    return x ** 3

def absolute(x): # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)
    
def higher_order_func(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_func('square')
print(result(3)) # 9
result = higher_order_func('cube')
print(result(3)) # 27
result = higher_order_func('absolute')
print(result(-3)) # 3

# You can see from the above example that the higher order function is returning different functions depending on the passed parameter.


# Python Closures
# Python allows a nested function to access the outer scope of the enclosing function. This is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below -
# Example
def add_ten():
    ten = 10
    def add(num):
        return num + 10
    return add

closure_result = add_ten()
print(closure_result(5)) # 15
print(closure_result(10)) # 20


# Python Decorators
# A decorator is a design pattern in python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

# Creating Decorators
# To create a decorator function, we need an outer function with an inner wrapper function.

# example
# Normal function
def greet():
    return 'Welcome to Canada'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greet)
print(g()) # WELCOME TO CANADA

# Using the same function above with a decorator
'''this decorator function is a higher order function that takes a function as a parameter'''
def uppercase_decorator_new(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper
@uppercase_decorator_new
def greet_new():
    return 'Welcome to Australia'
print(greet_new()) # WELCOME TO AUSTRALIA


# APPLYING multiple decorators to a Single Function
'''These decorators functions are higher order functions that take functions as parameters'''
#First decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second Decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to the USA'
print(greeting()) # ['WELCOME', 'TO', 'THE', 'USA']


# Accepting Parameters in Decorator Functions
# Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print('I live in {}'.format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(f_name, l_name, country):
    print('I am {} {}. I love to teach.'.format(
        f_name, l_name
    ))

print_full_name('Kush', 'Sin', 'Canada')


# Built-in Higher Order Functions
# Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce. Lambda functions can be passed as a parameter and the best use case of the lambda functions is in functions like map, filter and reduce.

# Python - Map Function
# The map() function is a built-in functioon that takes a function and iterable as parameters.

# syntax
# map(function, iterable)


# example 1
numbers = [1, 2, 3, 4, 5] # iterable because its a list can be iterated
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared)) # [1, 4, 9, 16, 25] - it calls square function on each item of the numbers list and maps them together - then, the result is converted into a list using list() function

# LEts apply it with a lambda function
numbers_squared_lambda = map(lambda x: x ** 2, numbers) # first one is a function, second one is the iterable
print(list(numbers_squared_lambda)) # [1, 4, 9, 16, 25] - same result with less hassle


# example 2
numbers_str = ['1', '2', '3', '4', '5']  # iterable - numbers in string format
numbers_int = map(int, numbers_str)
print(list(numbers_int)) # [1, 2, 3, 4, 5] - every number is converted into am int using the int function


# example 3
names = ['Kush', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased)) # ['KUSH', 'LIDIYA', 'ERMIAS', 'ABRAHAM'] - all names changes to upper case characters

# We can use the same function but using lambda function
names_upper_cased_lambda = map(lambda name: name.upper(), names)
print(list(names_upper_cased_lambda)) # ['KUSH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']


# What map actually does is iterate over a list or iterable. For instance, it changes the namess to upper case and returns a new list with the updated/changes values.


# Python - Filter Function
# The filter() function calls the specified function which returns boolean for each item of the specified iterable(list) - true or false. It filters the items that satisfies the filtering criteria.

# syntax
# filter(function, iterable)

# example 1
