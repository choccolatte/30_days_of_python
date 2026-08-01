# built-in functions

# abs() - returns the absolute (positive) value of a number
# all() - returns True if all elements in an iterable are True
# any() - returns True if at least one element in an iterable is True
# ascii() - returns a string with non-ASCII characters escaped
# bin() - converts an integer to a binary string
# bool() - converts a value to True or False
# breakpoint() - pauses execution and starts the debugger
# bytearray() - creates a mutable sequence of bytes
# bytes() - creates an immutable sequence of bytes
# callable() - checks if an object can be called like a function
# chr() - returns the character for a Unicode code point
# classmethod() - defines a method that belongs to the class, not an instance
# compile() - compiles source code into a code object
# complex() - creates a complex number
# delattr() - deletes an attribute from an object
# dict() - creates a dictionary
# dir() - lists the attributes and methods of an object
# divmod() - returns the quotient and remainder of division
# enumerate() - adds an index to each item in an iterable
# eval() - evaluates and executes a Python expression
# exec() - executes dynamically generated Python code
# filter() - filters elements that satisfy a condition
# float() - converts a value to a floating-point (decimal) number
# format() - formats a value into a specified string format
# frozenset() - creates an immutable set
# getattr() - gets the value of an object's attribute
# globals() - returns the global symbol table as a dictionary
# hasattr() - checks if an object has a specified attribute
# hash() - returns the hash value of an object
# help() - displays documentation for an object
# hex() - converts an integer to a hexadecimal string
# id() - returns the unique identity of an object
# input() - asks for and returns user input as a string
# int() - converts a value to an integer
# isinstance() - checks if an object is an instance of a class
# issubclass() - checks if one class is a subclass of another
# iter() - returns an iterator for an iterable
# len() - returns the number of items in an object
# list() - creates a list
# locals() - returns the local symbol table as a dictionary
# map() - applies a function to every item in an iterable
# max() - returns the largest value
# memoryview() - creates a memory view object without copying data
# min() - returns the smallest value
# next() - returns the next item from an iterator
# object() - creates a base object
# oct() - converts an integer to an octal string
# open() - opens a file
# ord() - returns the Unicode code point of a character
# pow() - returns a number raised to a power
# print() - displays output on the screen
# property() - defines managed attributes using getter/setter methods
# range() - generates a sequence of numbers
# repr() - returns the official string representation of an object
# reversed() - returns a reverse iterator
# round() - rounds a number to the nearest value
# set() - creates a set of unique elements
# setattr() - sets the value of an object's attribute
# slice() - creates a slice object
# sorted() - returns a sorted list from an iterable
# staticmethod() - defines a method that doesn't receive self or cls
# str() - converts a value to a string
# sum() - returns the sum of all items in an iterable
# super() - gives access to methods of a parent class
# tuple() - creates a tuple
# type() - returns the type of an object
# vars() - returns the __dict__ of an object as a dictionary
# zip() - combines multiple iterables element by element
# __import__() - imports a module dynamically


# Variables - store data in a computer memory. Mnemonic variables are recommended to use - which is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special characters, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z) but a more descriptiev name (firstName, lastName, age, country) is highly reecommended.

# Variable naming rules in Python -
# 1. A variable name must start with a letter or the underscore charcter.
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
# 4. Variable names are case-sensitive (firstName, firstname, FirstName, and FIRSTNAME are all different variable names.)

# Variable declaration is when we assign a certain data type to a variable. For instance, here, we assign a name (string) to a variable called first_name. Assigning means storing data in the variable. The equal sign in Python is not equality as in Maths.

first_name = 'Kush'
last_name = 'Sin'
country = "India"
city = 'New Delhi'
age = 2500
is_married = False
skills = ['HTML', 'Python', 'Swift', 'Java']
person_info = {
    'firstName': 'Kush',
    'lastName': 'Sin',
    'country': 'India',
    'city': 'New Delhi',
}

print(len('Hello world!'))

# print() can take unlimited number of arguments - Arguments is a value which we can pass or put inside the function's paranthesis.

print("First name:", first_name)
print("Last name:", last_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Married:", is_married)
print("Skills:", skills)
print("Person information:", person_info)


# Declaring Multiple Variable in a Line
# Multiple variables can also be declared in one line:
fname, lname, state, is_age, is_single = 'Kush', 'Sin', 'Delhi', 2500, False

# getting user input using the input() built-in function
# let us assign the data we get from a user into the fName, and other variables.
fName = input("Enter your name: ")
fName_age = input("Enter your age: ")

print(fName)
print(fName_age)

# Data Types
# there are several data types in python - to identify the data type we use the type() built-in function. In programming, its all about data types.

# Checking data types and Casting 
# Check data types - to check the data types of certain data/variable we use the type.
# example -

# printing the data types of the variables we discussed earlier
print(type(first_name))
print(type(age)) 
print(type(skills))
print(type(person_info))

# Casting - Converting one data type into another data type is casting. We use int(), float(), str(), list, set to convert one data type to another. When we do arithmetic operations, string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string.

# int to float
print("Age: ", age)
age_float = float(age)
print("Float age:", age_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
print(age)
age_str = str(age)
print(age_str)

# str to int or float
num_str = '100.54'
num_float = float(num_str)
num_int = int(num_float)
print(num_str)
print(num_float)
print(num_int)

# str to list
fnameNew = 'Kush'
print(fnameNew)
fnameNew_to_list = list(fnameNew)
print(fnameNew_to_list)

# Numbers - numbers are data tyhpes in python - 
# Integers - integer(negative, zero, and positive) numbers - example - -3, -2, -1, 0, 1, 2, 3
# Floating point numbers (decimal numbers) - example - -2.5, -1.5, 0.01, 1.11, 2.12
# Complex numbers - example - 1+j, 2+4j, 1-1j

# Exercises - Level 1 - Day 2

# Declare a first name variable and assign a value to it
firstName = "Kush"

# Declare a last name variable and assign a value to it
lastName = "Kai"

# Declare a full name variable and assign a value to it
fulName = firstName + lastName

# Declare a country variable and assign a value to it
cont = "Canada"

# Declare a city variable and assign a value to it
cit = "Vancouver"

# Declare an age variable and assign a value to it
agee = 2500

# Declare a year variable and assign a value to it
yr = 2026

# Declare a variable is_married and assign a value to it
isMarried = False

# Declare a variable is_true and assign a value to it
isTrue = False

# Declare a variable is_light_on and assign a value to it
isLightOn = True

# Declare multiple variable on one line
skills = ["Java", "Python", "React"]


# Exercises - Level 2 - Day 2

# Check the data type of all your variables using type() built-in function
print(type(firstName))
print(type(lastName))
print(type(isMarried))
print(type(skills))
print(type(isLightOn))
print(type(cont))
print(type(cit))
print(type(isTrue))

# Using the len() built-in function, find the length of your first name
print(len(firstName))
print(len(lastName))

# Compare the length of your first name and your last name
print(len(first_name) - len(lastName))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = (num_one + num_two)

# Subtract num_two from num_one and assign the value to a variable diff
diff = (num_one - num_two)

# Multiply num_two and num_one and assign the value to a variable product
product = (num_two * num_one)

#Divide num_one by num_two and assign the value to a variable division
division = (num_one / num_two)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = (num_two % num_one)

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = (num_one ** num_two)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = (num_one // num_two)

# The radius of a circle is 30 meters. Calculate the area of a circle and assign the value to a variable name of area_of_circle
rad = 30
area_of_circle = (3.14 * (rad * rad))

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * (3.14 * rad)

# Take radius as user input and calculate the area.
radUsr = int(input("Enter radius of circle: "))
area_of_circleUsr = (3.14 * (radUsr * radUsr))

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
firstNameUsr = input("Enter first name: ")
lastNameUsr = input("Enter last name: ")
cityUsr = input("Enter city: ")
countryUsr = input("Enter country: ")
ageUsr = input("Enter age: ")

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')