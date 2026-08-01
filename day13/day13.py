# Day 13 - List Comprehension

# List Comprehension in python is a compact way of creating a list from a sequence. It is a short way to create a new list. List Comprehension is considerably faster than processing a list using the for loop.

# syntax
# [expression for i in iterable if condition]

# example
# one way to do it
language = 'Python'
lst = list(language) # converitng the stirng to list
print(type(lst)) # its type is now List
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']

# second way of list comprehension - both these ways will produce the same result
lst2 = [i for i in language]
print(type(lst2)) # its type is now List
print(lst2) # ['P', 'y', 't', 'h', 'o', 'n']


# example 2
# for instance, if you want to generate a list of numbers

# generating numbers 
nums = [i for i in range(11)] # to generate a list of numbers from 0 to 10
print(nums)

# it is also possible to do mathematical operations during iteration
squares = [i * i for i in range(11)] # will multiply each number with itself in the range so it becomes - [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# it is also possible to make a list of tuples
numstup = [(i, i * i) for i in range(11)] # here, i is num, i * i is num * num, so its - 1, 1 * 1 = 2, 2, 2 * 2 = 4 - but it will be given in a tuple - [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
print(numstup)


# example 3

# list comprehension cna be combined with if expression as well.

# generate even numbers
even_nums = [i for i in range(21) if i % 2 == 0] # # to generate even numbers list in range 0 to 21
print(even_nums)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# generating odd numbers
odd_nums = [i for i in range(21) if i % 2 != 0] # # to generate odd numbers in range 0 to 21
print(odd_nums) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# filter numbers - lets filter out the positive even numbers from the list below
num_pool = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10] 
positive_pool = [i for i in num_pool if i % 2 == 0 and i > 0] # to generate even numbers in range 0 to 21
print(positive_pool) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
neg_pool = [i for i in num_pool if i % 2 != 0 and i < 0]
print('Negative numbers from list:', neg_pool)
 
# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ num for row in list_of_lists for num in row]
print(flattened_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]



# Lmabda Function
# Lambda function is a small anonymous function without a name. It can take any numbers of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JS. Here, we need it when we want to write an anonymous function inside another function.


# Creating a Lambda function
# To create a Lambda function, we use lambda keyword, followed by a parameter(s), followed by an expression. 
# See the syntax and the example below. 
# Lambda function does not use return but it explicitly returns the expression.

# syntax
# x = lambda param1, param2, param3: param1 + param2 + param3 # storing the Lambda function inside a variable, which we can call like a normal function with arguments
# print(x(arg1, arg2, arg3))


# example
# named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(12, 65))

# now, lets change the above function to a lambda function
add_two_nums2 = lambda a, b: a + b
print(add_two_nums2(12, 56))

# Self invoking lambda function
print((lambda a,b: a + b)(2, 3)) # 5 - need to encapsulate it in print to see the actual result in the console

square = lambda x: x ** 2
print(square(12))

cube = lambda y: y ** 3
print(cube(9))

# multiple variables
mult_var = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(mult_var)


# Lambda Function inside Another Function
# Using a lambda function inisde another function

def power(x):
    return lambda n: x ** n
cube = power(2)(3) # function power now needs 2 arguments to run, in seperate rounded brackets - 2 is given to x and 3 is given to lambda's n
print(cube) #8
two_power_of_five = power(2)(5)
print(two_power_of_five) # 32


# 💻 Exercises: Day 13
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
num_new = [i for i in numbers if i > 0]
print(num_new)

# Flatten the following list of lists of lists to a one dimensional list :
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
one_d_lst = [num for row in list_of_lists for num in row]
print(one_d_lst)

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
num_tuple = [(num, num * num) for num in range(11)]
print(num_tuple)



# Flatten the following list to a new list:

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# Change the following list to a list of dictionaries:

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
# Change the following list of lists to a list of concatenated strings:

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# Write a lambda function which can solve a slope or y-intercept of linear functions.

