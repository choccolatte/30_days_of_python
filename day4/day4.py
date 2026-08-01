# Strings

# Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quotes are strings. THere are different string methods and built in functions to deal with string data types. 
# To check the length of a string, use the len() method.

# Creating a String
letter = 's'
print(letter)
print(len(letter))

greeting = "Helo world!"
print(greeting)
print(len(greeting))

# Multiline string is created by using triple single(''') or triple double quotes (""").

multiline_Str = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_Str)


# String Concatenation
# We can connect strings together. merging or connecting strings is called concatenation.
fName = "Kush"
lName = "Kai"
space = ' '
fuName = fName + space + lName
print(fuName)

# checking the length of a string using len() and built-in function
print(len(fName))
print(len(lName))
print(len(fName) > len(lName))
print(len(fuName))


# Escape Sequences in Strings
# in python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:
# \n - new line
# \t - tab means (8 spaces)
# \\ - backslash
# \' - single quote
# \" - double quote

# now, let us see the use of the above escape sequences with examples -
print('I hope everyone is enjoying the day.\nAre you okay?')
print('Day: Monday\tWhats to do today?')
print('Day1\t5\t5')
print('This is a backslash - \\. And this is a double quotes \", and a single quotes now \'')


# String formatting
# Old style string formatting (% Operator)

# In python, there are many ways of formatting strings. In this section, we will cover some of them. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".
#   - "%s" - String (or any object with a string representation, like numbers )
#   - "%d" - integers
#   - "%f" - floating point numbers
#   - "%.number of digitsf" - floating point numbers with fixed precision

# Strings only
fNameN = 'Kush'
lNameN = 'Sin'
lang = 'Python'
formatted_string = 'I am %s %s. I am learning %s. %(fNameN, lNameN, lang)'
print(formatted_string)

# Strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string_new = 'The area of circle with a radius of %d is %.2f.' %(radius, area) # here, 2 refers the 2 significant digits after the decimal dot/point

py_lib = ['Django', 'Flask', 'NumPy', 'Pandas']
formatted_string_lib = 'The following are the python libraries: %s' %(py_lib)
print(formatted_string_lib) # 'The following are the python libraries: ['Django', 'Flask', 'NumPy', 'Pandas']'



# New Style String Formatting (str.format)
# This format was introduced in Python version 3.
fName = 'Kush'
lName = 'Sin'
lang = 'Python'
form_strings = 'I am {} {}. I teach {}'.format(fName, lName, lang)
print(form_strings)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))
print('{} / {} = {:.2f}'.format(a, b, a/b)) # limits the remainder to 2 values
print('{} % {} = {}'.format(a, b, a%b))
print('{} // {} = {}'.format(a, b, a//b))
print('{} ** {} = {}'.format(a, b, a**b))

# Strings and numbers
radius = 20
pi = 3.14
area = pi * radius ** 2
form_str_new = 'The area of circle with radius {} is {:.2f}.'.format(radius, area)
print(form_str_new)


# String Interpolation / f-Strings (Python 3.6+)
# Another new string formatting is string interpolation, f-strings. Strings start with f and we can inject the data in their corresponding positions.
a = 4
b = 3
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')


# Python strings as Sequences of Characters
# Python Strings are sequences of characters, and share their basic methods of access with other python ordered sequences of objects - lists and tuples. The simplest way of extracting single characters from Strings (and individual members from any sequence) is to unpack them into corresponding variables.

# Unpacking Characters
lang = 'Python'
a, b, c, d, e, f = lang # unpacking sequence charactes into variables
print(a) # P
print(b) # y 
print(c) # t
print(d) # h
print(e) # o
print(f) # n


# Accessing Charactes in Strings by Index
# in programming, counting starts from zero(0). Therefore, the first letter of a string is at zero index, and the last letter of the string is the length of the string minue one (because we started from 0).
# P = 0 
# y = 1
# t = 2
# h = 3
# o = 4
# n = 5

lang_new = 'Python'
firstLetter = lang_new[0]
print(firstLetter) # P
secondLetter = lang_new[1]
print(secondLetter) # y
last_index = len(lang_new) -1
last_letter = lang_new[last_index]
print(last_letter) # n

# if we want to start from right end, we can use negative indexing. -1 is the last index, -2 is the second last and so on...
language = 'Python'
lastLetter = language[-1]
print(lastLetter) # n
secondLastLetter = language[-2]
print(secondLastLetter) # o


# Slicing Python Strings
# in python, we can slice strins into substrings.
languageNew = 'Python'
first_3 = languageNew[0:3] # here, it starts at zero index - P, and up to 3 but not including 3, so it stops at h but will print till t
last_3 = languageNew[3:6]
print(last_3) #hon
#another way to do it is 
last3 = languageNew[3:] # this will take it to the end since we havent provided the end to slice
print(last3) #hon


# Reversing a String
# we can easily reverse a string in Python.
greet = 'Hello world'
print(greet[::-1]) # dlrow olleH

# Skipping Characters while Slicing
# It is possible to skip characters while slicing by passing step argument to slice method.
langu = 'Python'
pto = langu[0:6:2] # it starts at 0, goes till 6, and skips every second item - yhn
print(pto) # Pto


# String Methods
# THere are many string methods which allow us to format strings. See some of the string methods in the following examples:

# capitalize() - Converts the first character of the string to capital letter.
challenge = 'thirty days of python'
print(challenge.capitalize()) # Thirty days of python

# count() - returns occurences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end if the last index to count.
coun = 'thirty days of python'
print(coun.count('y')) # 3
print(coun.count('y', 7, 14)) # 1
print(coun.count('th')) # 2

# endswith() - checks if a string ends with a specified ending.
endsw = 'thirty days of python'
print(endsw.endswith('on')) # True
print(endsw.endswith('tion')) # False

# expandtabs() - replaces the tab character with spaces, default tab size is 8. It takes the tab size argument
tabss = 'thirty\tdays\tof\tpython'
print(tabss.expandtabs()) # thirty  days    of  python
print(tabss.expandtabs(10)) # thirty        days        of      python

# find() - returns the index of the first occurence of a substring, if not found, returns -1.
fin = 'thirty days of python'
print(fin.find('y')) # 5
print(fin.find('th')) # 0
print(fin.find('zzz')) # -1

# rfind() - returns the index of the last occurrence of a substring, if not found returns -1.
rfin = 'thirty days of python'
print(rfin.rfind('y')) # 16
print(rfin.rfind('zzz')) # -1

# format() - formats the string into a nicer output.
fir_name = 'Kush'
las_name = 'Sin'
age = 2500
job = 'engineer'
countr = 'Canada'
sentence = 'I am {} {}. I am a {} and I am {} years old. I live in {}.'.format(fir_name, las_name, job, age, countr)
print(sentence)

radius = 10
pi_new = 3.14
are = pi_new * radius ** 2
res = 'The area of a circle with radius {} is {}'.format(radius, are)
print(res)

# index() - returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found, it raises a valueError.
ind = 'thirty days of python'
sub_str = 'da'
print(ind.index(sub_str)) # 7
# print(ind.index(sub_str, 9)) # error

# rindex() - returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1).
rind = 'thirty days of python'
sub_str2 = 'da'
print(rind.rindex(sub_str2)) # 7
# print(rind.rindex(sub_str2, 9)) # error
print(rind.index('on', 8)) # 19

# isalnum() - checks alphanumeric characters
chal = 'thirtydayspython'
print(chal.isalnum()) # true

chal2 = '30daysofpython'
print(chal2.isalnum) # true

chal3 = 'thirty days of python'
print(chal3.isalnum()) # false, space is not an alphanumeric character

chal4 = 'thirty days of python 2026'
print(chal4.isalnum()) # false


# isalpha() - checks if all string elements are alphabet charactes (a-z and A-Z)
chal_new = 'thirty days of python'
print(chal_new.isalpha()) # false, spaces are once again excluded

chal_new2 = 'thirtydaysofpython'
print(chal_new2.isalpha()) # true

chal_new3 = 1233456
# print(chal_new3.isalpha()) # error - false, because its numeric values


# isdecimal() - checks if all characters in a string are decimal (0-9)
chal_dec = 'thirty days of python'
print(chal_dec.isdecimal()) # false

chal_dec2 = '123'
print(chal_dec2.isdecimal()) # true - its decimal strings 0-9

chal_dec3 = '\u00B2'
print(chal_dec3.isdecimal()) # true - contains decimal values

chal_dec4 = '12 3'
print(chal_dec4.isdecimal()) # false, spaces are not allowed


# isdigit() - checks if all characters in a string are numbers (0-9, and some other unicode characters for numbers)
chal_dig = 'Thirty'
print(chal_dig.isdigit()) # false - since its a string

chal_dig2 = '50'
print(chal_dig2.isdigit()) # true - since its numbers/digits

chal_dig3 = '\u00B2'
print(chal_dig3.isdigit()) # true - since its numbers 


# isnumeric() - checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like 1/2)
num = '10'
print(num.isnumeric()) # true

num2 = '\u00BD' # 1/2
print(num2.isnumeric()) # true

num3 = '10.5'
print(num3.isnumeric()) # false - we've got a decimal point here


# isidentifier() - checks for a valid identifier - it checks if a string is a valid variable name
chal_id = '30daysofpython'
print(chal_id.isidentifier()) # false, because it starts with a number

chal_id2 = 'thirty_days_of_python'
print(chal_id2.isidentifier()) # true


# islower() - checks if all alphabet characters in the string are in lowercase
chal_low = 'thirty days of python'
print(chal_low.islower()) # true

chal_low2 = 'THirty days of Python'
print(chal_low2.islower()) # false


# isupper() - checks if all alphabet characters in the string are in uppercase
chal_up = 'thirty days of python'
print(chal_up.isupper()) # false
chal_up2 = 'THIRTY DAYS OF PYTHON'
print(chal_up2.isupper()) # true


# join() - returns a concatenated string
web_tech = ['HTMML', 'CSS', 'JS', 'React']
result = ' '.join(web_tech)
print(result) # HTML CSS JS React

back_end = ['Python', 'Java', 'C#']
result_new = '# '.join(back_end)
print(result_new)


# strip() - removes all given characters starting from the beginning and end of the string
chal_str = 'thirty days of pythooooonnn'
print(chal_str.strip('noth')) #irty days of py


# replace() - replaces substring with a given string
chal_rep = 'thirty days of python'
print(chal_rep.replace('python', 'programming')) # thirty days of programming


# split() - splits the string, using given string or space as a seperator
chal_sep = 'thirty days of python'
print(chal_sep.split()) # ['thirty', 'days', 'of', 'python']

chal_sep2 = 'thirty, days, of, python'
print(chal_sep2.split(', ')) # ['thirty', 'days', 'of', 'python']


# title() - returns a title cased string
chal_tit = 'thirty days of python'
print(chal_tit.title()) # Thirty Days Of Python


# swapcase() - converts all uppercase characters to lowercase and all lowercase characters to uppercase
chal_swap = 'thirty days of python'
print(chal_swap.swapcase()) # THIRTY DAYS OF PYTHON

chal_swap2 = 'Thirty Days Of Python'
print(chal_swap2.swapcase()) # tHIRTY dAYS oF pYTHON


# startswith() - checks if string starts with the specified string
chal_start = 'thirty days of python'
print(chal_start.startswith('thirty')) # true

chal_start2 = '30 days of python'
print(chal_start2.startswith('thirty')) # false


# Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str_to_concat = ['Thirty', 'Days', 'Of', 'Python']
concat_str = ' '.join(str_to_concat)
print(concat_str)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str_to_concat2 = ['Coding', 'For', 'All']
concat_str2 = ' '.join(str_to_concat2)
print(concat_str2)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
upr = company.upper()
print(upr)

# Change all the characters to lowercase letters using lower() method.
lwr = company.lower()
print(lwr)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capt = company.capitalize()
titl = company.title()
swapc = company.swapcase()
print(capt)
print(titl)
print(swapc)

# Cut(slice) out the first word of Coding For All string.
print(company[1:-1])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
cont = company.find('Coding')
print(cont)

# Replace the word coding in the string 'Coding For All' to Python.
rep = company.replace('Coding', 'Python')
print(company)

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
le_str = 'Python for Everyone'
le_str.replace('Everyone', 'All')
print(le_str)

# Split the string 'Coding For All' using space as the separator (split()) .
str_new = 'Coding for all'
str_new.split(' ')
print(str_new)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
comps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
comps.split(',')
print(comps)

# What is the character at index 0 in the string Coding For All.
print(str_new[0])

# What is the last index of the string Coding For All.
print(str_new[-1])

# What character is at index 10 in "Coding For All" string.
print(str_new[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acr = 'Python For Everyone'
new_acr = acr.split(' ') # ["python", "For", "Everyone"]
new_acr1 = new_acr[0][0]
new_acr2 = new_acr[1][0]
new_acr3 = new_acr[2][0]
new_acr_formed = new_acr1 + new_acr2 + new_acr3
print(new_acr_formed)

# Create an acronym or an abbreviation for the name 'Coding For All'.

# Use index to determine the position of the first occurrence of C in Coding For All.
print(str_new.find('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(str_new.find('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
new_str = 'Coding For All People'
print(new_str.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_stat = 'You cannot end a sentence with because because because is a conjunction'
print(new_stat.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_sta = 'You cannot end a sentence with because because because is a conjunction'
print(new_sta.rfind('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sta.find('because'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Does 'Coding For All' start with a substring Coding?
new_sub = 'Coding For All'
print(new_sub.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print(new_sub.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_new_sub = '   Coding For All      '
print(new_new_sub.strip())

# Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python
print('30daysofpython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
py_frame = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
res_fra = '# '.join(py_frame)
print(res_fra)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Kush\t2500\tVancouver\tCanada')

# Use the string formatting method to display the following: The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
z = 8
y = 6
print(f'{z} + {y} = {z + y}')
print(f'{z} - {y} = {z - y}')
print(f'{z} * {y} = {z * y}')
print(f'{z} / {y} = {z / y:.2f}')
print(f'{z} % {y} = {z % y}')
print(f'{z} // {y} = {z // y}')
print(f'{z} ** {y} = {z ** y}')