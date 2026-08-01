# Day 11 - Functions

#Till now, we've seen many built-in python functions. But now, we will focus custom fucntions. 

# A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.


# Declaring and Calling a Function
# When we make a function, we call it declaring a function. When we start using it, we call it calling or invoking a funciton. Functions can be declared with or without parameters.

# syntax
# Declaring a function
# def function_name():
#     codes
#     codes
# # Calling a function
# function_name()


# Function without Parameters
# Function can be declared without parameters

# example
def generate_full_name():
    f_name = "Kush"
    l_name = "Sin"
    space = ' '
    full_name = f_name + space + l_name
    print(full_name)
generate_full_name() # Calling a function

def add_two_nums():
    num_one = 2
    num_two = 5
    total = num_one + num_two
    print(total)
add_two_nums() # Calling the function


# Function Returning a Value - Part 1
# Function return values using the return statement. If a function has no return statement, it returns None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.

def gen_full_name():
    f_name = 'Kush'
    l_name = 'Sin'
    space = ' '
    full_name = f_name + space + l_name
    return full_name
print(gen_full_name()) # printing the returned value from the function call

def add_two_nums():
    num_1 = 10
    num_2 = 100
    total = num_1 + num_2
    return total
(add_two_nums())


# Functions with Parameters
# In a function, we can pass different data types (number, string, boolean, list, tuple, dictionary, or set) as parameters.

    # single parameters - if our function takes a parameter we should call our function with an argument.

    # syntax
    # Declaring a function
    # def function_name(parameter):
    #     codes
    #     codes
    # # Calling function
    # print(function_name(argument))

# Example
def greetings(name):
    message = name + ', welcome to this world.'
    return message
print(greetings('Kush'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(900))

def square_num(x):
    return x * x
print(square_num(900))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(100))

def sum_of_num(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_num(100))
print(sum_of_num(1000))

# Two Parameter - A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters - 

# syntax
# Declaring a function
# def func_name(para1, para2):
#     codes
#     codes
# # Calling a function
# print(func_name(arg1, arg2))

# example
def generate_full_name(f_name, l_name):
    space = ' '
    ful_name = f_name + space + l_name
    return ful_name
print('Full name:', generate_full_name('Kush', 'Sin'))

def sum_two_num(num1, num2):
    sum = num1 + num2
    return sum
print('Sum of numbers:', sum_two_num(100, 999))

def calculate_age(curr_year, birth_year):
    age = curr_year - birth_year
    return age
print('Age: ', calculate_age(2026, 1995))

def weight_of_object(mass, gravity):
    weight = str(mass * gravity) + ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(75, 9.81))


# Passing Arguments with Key and Value
# If we pass the arguments with a key and a value, the order of the arguments does not matter.

# syntax
# # Declaring a function
# def func_name(para1, para2):
#     codes
#     codes
# # Calling a function
# print(func_name(para1 = 'John', para2='Doe')) # the order of arguments


# example
def print_fullname(f_name, l_name):
    space = ' '
    ful_name = f_name + space + l_name
    return ful_name
print(print_fullname(l_name= 'Doe', f_name='John')) 

def add_two_nums(num1, num2):
    total = num1 + num2
    return total
print((add_two_nums(num2 = 10, num1=999)))


# Functions Returning a Value - Part 2
# If we do not return a value with a function, then our function is returning None by default. To return a value with a function, we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function/

# Returning a string - example
def print_name(f_name):
    return f_name
print(print_name('Kush'))

def print_full_name(f_name, l_name):
    space = ' '
    ful_name = f_name + space + l_name
    return ful_name
print(print_full_name('Kush', 'Sin'))


# Returning a number - example
def add_two_nums(n1, n2):
    total = n1 + n2
    return total
print(add_two_nums(19, 200))

def calc_age(curr_year, birth_year):
    age = curr_year - birth_year
    return age
print('Age:', calc_age(2030, 2000))


# Returning a Boolean - example
def is_even(num):
    if num % 2 == 0:
        return True # return stops further execution of the function, similar to break
    return False
print(is_even(109)) # False
print(is_even(10)) # True


# returning a list - example
def find_even_nums(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_nums(10))


# Function with Default Parameters
# Sometimes, we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

# syntax
# Declaring a function
# def func_name(param = value):
#     codes
#     codes
# # Calling a function
# func_name()
# func_name(arg)

# example
def greet(name = 'John'):
    msg = name + ', Welcome to Canada.'
    return msg
# Calling function
print(greet()) # default 
print(greet('Kush')) # given parameter

def generate_ful_name(f_name = 'John', l_name = 'Doe'):
    space = ' '
    ful_name = f_name + space + l_name
    return ful_name
print(generate_ful_name())
print(generate_ful_name('Kush', 'Sin'))

def calc_age(birth_year, curr_year = 2026):
    age = curr_year - birth_year
    return age
print(calc_age(1990))

def weight_of_object(mass, gravity = 9.81):
    weight = str(mass * gravity )+ ' N' # the value has to be changed to string before use
    return weight
print(weight_of_object(100, 1.62))


# Arbitary Number of Arguments
# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before tbe parameter name.

# syntax
# declaring a function
# def func_name(*args):
#     codes
#     codes
# # Calling a function
# func_name(param1, param2, param3, ...)


# example
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num # same as total = total + num
    return total
print(sum_all_nums(2, 200, 999, 100))


# Default and Arbitrary Number of Parameters in Functions
def generate_groups(team, *members):
    print(team)
    for member in members:
        print(member)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')


# Dictionary Unpacking
# You can call a function which has named arguments using a dictionary with matching key names. You do so using **.

# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location) :
    # Print a greeting message using the provided arguments
    print('Hi there', name, 'how is the weather in', location)

# Call the function using keyword arguments
greet(name = 'Alice', location ='New York')
# Output - Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {'name':'Alice', 'location':'New York'}

# call the function using dictionary unpacking
greet(**my_dict)

# The ** operator unpacks the dictionary, passing its key-value pairs as keyword arguments to the function.
# Output - Hi there Alice how is the weather in New York


# Arbitrary Number of Named Arguments
# You can also define a function to accept an arbitrary number of named arguments.

def arbitrary_named_args(**args):
    print('I received an arbitrary number of arguments, totaling', len(args))
    print('They are provided as a dictionary in my function:', type(args))
    print('Lets print them now:')
    for k, v in args.items():
        print(' * key:', k, 'value:', v)
arbitrary_named_args()

# Generally avoid this unless required as it makes it harder to understand what the function accepts and does.


# Function as a Parameter of Another Function
# You can pass functions around as parameterss
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27



# 💻 Exercises: Day 11
# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(n1, n2):
    total = n1 + n2
    return total
print(add_two_numbers(10, 11))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(radius):
    PI = 3.14
    area = PI * radius * radius
    return area
print(circle_area(9))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) == int:
            total += num
        else:
            return 'Not a valid number.'
    return total
print(add_all_nums(3, 4, 3))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def c_to_f():
    tempinput = int(input('Enter temp in C: '))
    to_f = (tempinput * 9/5) + 32
    return f'{tempinput} degrees C in F is: {to_f}'
print(c_to_f())
    
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ("Feb", 'February', 'Mar', 'March', 'Apr', 'April'):
        return 'Spring'
    elif month in ('May' or 'Jun' or 'June' or 'July' or 'Jul'):
        return 'Summer'
    elif month in ('Aug','August', 'Sep',  'September', 'Oct', 'October'):
        return 'Autumn'
    elif month in ('Nov', 'November', 'Dec', 'December', 'Jan', 'January'):
        return 'Winter'
    else:
        return 'Invalid month. Enter a valid month - Jan - Dec.'
print(check_season('Jan'))

# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.



# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 4, 5])

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]
def reverse_list(lst):
    lst_rev = []
    for item in reversed(lst):
        lst_rev.append(item)
    return lst_rev
print(reverse_list([1, 23, 3, 4, 55]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.
def capitalize_list_items(lst):
    rev_lst = []
    for item in lst:
        rev_lst.append(item.capitalize())
    return rev_lst
print(capitalize_list_items(['abc', 'apple']))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst):
    present_list = [1, 2, 3, 4, 5]
    for item in lst:
        present_list.append(item)
    return present_list
print(add_item([10, 9, 8, 7]))

# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
def add_items2(lst):
    food_stuff = ['Potato', 'Tomato', 'Mango',
     'Milk']
    for item in lst:
        food_stuff.append(item)
    return food_stuff
print(add_items2(['Potato', 'Tomato', 'Mango', 'Milk','Meat']))

# print(add_item(numbers, 5)) # [2, 3, 7, 9, 5]
# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item): 
    for item in lst:
        lst.remove(item)
    return lst
print(remove_item([2, 3, 7, 9, 5, 5, 4, 3, 2, 2, 12], 3))
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))



# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     # "Hello, Alice!"
# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# show_args(name="Alice", age=30, city="New York")
# # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# # Received: name: Bob, pet: Fluffy, the bunny
# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.