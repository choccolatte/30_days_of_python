# Day 15 - Python Type Errors

# When we werite code it is common that we make a type/error or some other common error. If our code fails to run, the Python interpreter will display a message, containing  feedback with information on where the problem occurs and the type of an error. It will also sometimes gives us suggestions on a possible fix. Understanding different types of errors in programming languages will help us to debug our code quickly and also it makes us better at what we do.
# Let us see the most common error types one by one. FIrst, let us open our Python interactive shell. For that, we need to go to terminal and write 'python3'. The python interactive shell will be opened. Now, we can write our code in the interactive shell and see the errors. Let us see the most common error types one by one.


# SyntaxError
# example 1 - SyntaxError
# print 'hello world' SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?


# As you can see we made a syntax error because we forgot to enclose the string with parantheses, and Python already suggests the solution. Lets fix it - SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
print('hello world') # hello world

# The error was a SyntaxError - after the code fix is executed without a hitch.
# Lets see more error types -


# NameError
# example 2 - NameError
# print(age) # NameError: name 'age' is not defined. Did you mean: 'age'?

# Here, we can see from the message above that the variable name age is not defined. Yes, its true that we did not define an age variable but we were trying to print it out. as if we had already declared it. Now, lets fix that by declaring it and assigning it with a value and then callling/using it.

age = 25
print(age) # 25

# Here, the type of error was a NameError - We debugged it by declaring the variable and assigning it a value. Now, the code runs without any error.


# IndexError
# example 3 - IndexError
# numbers = [1, 2, 3, 4, 5]
# print(numbers[5]) # IndexError: list index out of range

# In the example above - Python raises an IndexError - because the list has only indexes from 0 to 4 - so it was out of range.


# ModuleNotFoundError
# example 4 - ModuleNotFoundError
# import mathh # ModuleNotFoundError: No module named 'mathh'. Did you mean: 'math'?    

# In the example above, we added an extra 'h' in the module name - so Python raises a ModuleNotFoundError - because it could not find the module with that name. The error message also suggests the correct module name.

import math # Now, we have fixed the error by importing the correct module name - math. The code runs without any error.


# AttributeError
# example 5 - AttributeError
# import math
# math.PI # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# Here, we can see that we made a mistake - instead of writing pi, we tried to call PI - a constant from the math module. It raised an attribute error - which means that the attribute does not exist in the module. Lets fix it by changing PI to pi.
import math
math.pi

# Now, when we call pi from the math module, we get our desired result without any error. The type of error was an AttributeError - which we debugged by calling the correct attribute name.


# KeyError
# example 6 - KeyError
# person = {'name': 'John', 'age': 25}
# print(person['gender']) # KeyError: 'gender'

# As you can see in the example above, we tried to access a key that does not exist in the dictionary. It raised a KeyError - which means that the key does not exist in the dictionary. Lets fix it by adding the key 'gender' to the dictionary.
person = {'name': 'John', 'age': 25, 'gender': 'male'}
print(person['gender']) # male
# we have debugged the KeyError by adding the key 'gender' to the dictionary. Now, the code runs without any error.


# TypeError
# example 7 - TypeError
# print('4' + 3) # TypeError: can only concatenate str (not "int") to str

# In the example above, a TypeError is raised because we cannot add a nnumber to a string. FIrst solution would be to convert the string to an int or float. Another solution would be to convert the number to a string - the result then would be '43'. Let us follow the first fix - 
4 + int('3') # 7 - the string is converted to an int and then added to the number. The code runs without any error.
4 + float('3') # 7.0 - the string is converted to a float and then added to the number. The code runs without any error.

# Error is removed/fixed adn we got our result we expected. The type of error was a TypeError - which we debugged by converting the string to an int or float.


# ImportError
# example 8 - ImportError
# from math import power # ImportError: cannot import name power

# There is no function named power in the math module - so it raised an ImportError. Lets fix it by importing the correct function name - pow.
from math import pow # Now, we have fixed the error by importing the correct function name - pow. The code runs without any error.
pow(2, 3) # 8.0 - the pow function is called with the correct parameters and returns the expected result without any error.


# ValueError
# example 9 - ValueError
# int('4a') # ValueError: invalid literal for int() with base 10: '4a'

# In this case, we cannot change the given string to a number, because of the 'a' letter in the string. So, it raised a ValueError - which means that the value is not valid for the given function. Lets fix it by changing the string to a valid number.
int('4') # 4 - the string is converted to an int and returns the expected result without any error. The type of error was a ValueError - which we debugged by changing the string to a valid number.        


# ZeroDivisionError
# example 10 - ZeroDivisionError
# 10 / 0 # ZeroDivisionError: division by zero

# We cannot divide a number by zero - so it raised a ZeroDivisionError - which means that we cannot divide by zero. Lets fix it by changing the denominator to a non-zero number.
10 / 2 # 5.0 - the division is performed with a non-zero denominator



# Exercises: Day 15

# Open you python interactive shell and try all the examples covered in this section.