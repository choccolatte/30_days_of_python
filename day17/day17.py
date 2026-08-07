# Exception Handling

# Python uses try and except to handle errors gracefully. A graceful exit (or graceful error handling) of errors is a simple programming idiom - a program detects a serious error condition and 'exits gracefully', in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this makes our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

# We have covered the different python error types in the previous section. If we use try and except in our program, then it will not raise errors in those blocks.


try:
    {
        # run this code 
    }
except: # may or may not have a condition
    {
        # execute this code when there is an Exception
    }
else:
    {
        # no exceptions? Run this code
    }
finally:
    {
        # always run this code
    }

# code sample example
# try: 
#     # code in this block if things go well
# except:
#     #  code in this block run if things go wrong

# example
try: 
    print(10 + '5')
except:
    print('Something went wrong')

# IN the example above, the second operand is a string. We could change it to a float or int to add it with the number to make it work. But without any changes, the second block, except, will be executed.

# Example
try:
    name = input('Enter your name: ')
    year_born = input('Enter year you were born in: ')
    age = 2026 - year_born
    print(f'You are {name} and you are {age} years old.')
except:
    print('Something went wrong')

# In the example above, the exception block will run and we do not know exactly the problem. To analyze the problem, we can use the different error types with except block.

# In the following example, it will handle error and will also tell us the kind of error raised.

try:
    name_new = input('Enter name: ')
    yr_born = input('Enter year born: ')
    age_new = 2026 - yr_born
    print(f'You\'re {name_new} and you are {age_new} years old.')
except TypeError:
    print('Type error occured.')
except ValueError:
    print('Value error occured.')
except ZeroDivisionError:
    print('Zero division error occcured.')


# In the code above the output is going to be TypeError - now, lets add an aditional block.

try:
    nme = input('Enter name: ')
    yr_b = input('Enter year born in: ')
    ag = 2026 - yr_b
    print(f'You are {nme} and you are {ag} years old')
except TypeError:
    print('Type error occured.')
except ValueError:
    print('Value error occured.')
except ZeroDivisionError:
    print('Zero division error occured.')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')


# We can also shorten the code above
import datetime
try:
    name_nw = input('Enter name: ')
    yr_br = int(input('Enter year born in: '))
    curr_time = datetime.datetime.now()
    age_nw = curr_time.year - yr_br
    print(f'You are {name_nw} and you are {age_nw} years old.')
except Exception as e:
    print(e)


# Packing and Unpacking Arguments in Python
# We use two operators:
    # * for tuples
    # ** for dictionaries - becaue of key adn value pairs

# Let us write an example below - it only takes only arguments but we have a list. We can unpack the list and changes to argument.


# Unpacking
# Unpacking Lists

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = range(5) # gives 1 - 4 excluding 5
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e' - because we didnt unpack a list using *


# When we run this code, it raises an error, because this function takes numbers (not a list) as arguments, let us unpack/destructure the list properly this time -
def sum_of_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5] # range(6)
print(sum_of_nums(*lst)) # 15


# We can also use unpacking in the range built-in function that expects a start and an end
nums_range = range(2, 7) # normal call with seperate arguments
print(list(nums_range)) # [2, 3, 4, 5, 6]
args = [2, 7]
nums_n = range(*args) # call with arguments unpacked from a list
print(nums_n)


# A list or a tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Canada']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest) # # Finland Sweden Norway ['Denmark', 'Iceland', 'Canada']
nums_ran = range(8)
one, *mid_nums, last = nums_ran
print(one, mid_nums, last) #  1 [2, 3, 4, 5, 6] 7


# Unpacking Dictionaries


