# Day 9 - Conditionals

# By default, statements in Python script are executed sequentially from top to bottom. If the processing logic requires so, the sequential flow of execution can be altered in two ways -
    # COnditional Execution - a block of one or more statements will be executed if a certain expression is true.
    # Repetitive Execution - a block of one or more statements will be repetitively executed as long as a certain expression is true. Here, we will cover if, else, elif statements. The comparison and logical operators from earlier will be used and helpful here.


# If condition
# In Python and other programming languages the key word if is used to check if a condition is true, and to execute the block code. Remember the indentation after teh colon.

# syntax
# if condition:
#     this part of code runs for truthy conditions - conditions that are true

# example 1
a = 3
if a > 0:
    print('A is a positive number') # prints - A is a positiv number because the condition is met

# Here, you cna see 3 is greater than 0. The condition was true and the block code was executed. However, if the condition is false, we should have another block, which is going to be else - which executes only after the if condition turns out to be false.


# If Else
# If condition is true, the first block will be executed, if not then the else condition will run.

# syntax
# if condition:
#     this part of the code runs for truthy conditions
# else:
#     this part of the code runs for flasy conditions

# example
b = 3
if b < 0:
    print('A is a negative number')
else:
    print("A is a positive number")

# The condition above proves false, therefore the else block was executed. But what if our condition is more than just two? We could then use elif.


# If Elif Else
# In our daily lives, we make decisions on everyday. We make decisions not by checking one or two conditions, but multiple conditions. As similar to life, programming is also full of conditions, we use elif when we have multiple conditions.

# syntax
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# example
c = 0
if c > 0:
    print('C is a positive number')
elif c < 0:
    print('C is a negative number')
else:
    print('C is 0')

# in shorthand 
# syntax
# code if condition else code

# example
d = 3
print('D is positive') if d > 0 else print('D is negative') # here, first condition is met - so D positive is printed


# Nested Conditions
# COnditions can be nested as well - which means condition within a condition

# syntax
# if condition:
#     code
#     if condition:
#         code

# example
e = 9
if e > 0:
    if e % 2 == 0:
        print('E is a positive and even integer')
    else:
        print('E is a positive number')
elif e == 0:
    print('E is 0')
else:
    print('E is a negative number')

# We can avoid writing nested condition by using logical operator and.


# If COndition and Logical Operators
# syntax
# if condition and condition2:
#     code

# example
f = 1000
if f > 0 and f % 2 == 0:
    print('F is an even integer and a positive number')
elif f > 0 and f % 2 != 0:
    print('F is a positive number and an odd integer')
elif f == 0:
    print('F is 0')
else:
    print('F is a negative number')


# If and Or Logical Operators
# syntax
# if condition or condition2:
#     code

# example
user = 'admin'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Access Granted')
else:
    print('Access Denied!')



# Exercises: Day 9

# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input('Enter your age:' ))
if age >= 18:
    print('You are old enough to drive!')
else:
    print(f'Wait for {18 - age} years to drive.')

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 25
ur_age = int(input('Enter your age: '))
if my_age > ur_age:
    if my_age - ur_age == 1:
        print('I am 1 year older than you.')
    else:
        print(f'I am {my_age - ur_age} years older than you.')
elif my_age == ur_age:
    print('We are the same age!')
else:
    print(f'You are {ur_age - my_age} years older than me.')

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
n1= int(input('Enter num1: '))
n2= int(input('Enter num2: '))
if n1 > n2:
    print(f'{n1} is greater than {n2}')
elif n2 < n1:
    print(f'{n2} is greater than {n1}')
else:
    print(f'{n1} is equal to {n2}')


# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input('Enter current month: ')
if month == 'September' or month == 'October' or month == 'November':
    print('Its Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('Its Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('Its Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('Its Summer')
else:
    print('Invalid month')

# The following list contains some fruits:
# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input('Enter fruit name: ')
if user_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(user_fruit)
    print(fruits)


# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
#         person={
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
#     }

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:

# Asabeneh Yetayeh lives in Finland. He is married.

person = {
    'first_name': 'Kush',
    'last_name': 'Sin',
    'age': 250,
    'country': 'Canada',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][2])
else:
    print('Skills key not found')

#  If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

frontend = ['Javascript', 'React']
backend = ['MongoDB', 'Node', 'Python']
full = ['React, Node', 'MongoDB']
if all(skill in person['skills'] for skill in frontend):
    print('He is a front end developer')
elif all(skill in person['skills'] for skill in backend):
    print('He is a backend developer')
elif all( skill in person['skills'] for skill in full):
    print('He is a fullstack developer')
else:
    print('Unknown title')

#  * If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] == False and person['country'] =='Canada':
    print(f'{person['first_name']} {person['last_name']} lievs in {person['country']}. He is NOT married.')
else:
    print(f'The person is married and doesnt live in {person['country']}')