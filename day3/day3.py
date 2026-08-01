# Boolean
# A boolean data type represents one of the two values - True or False.
print(True)
print(False)

# Operators
# Python supports several types of operators.

# Assignment Operators
# Assignment Operators are used to assign value to variables. Let us take "=" as an example. Equals sign in maths shows that two values are equal (of equal value), however, in Python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. 

# Arithmetic Operators
# Addition (+) - a + b
# Subtraction (-) - a - b
# Multiplication (*) - a * b
# Division (/) - a / b
# Modulus (%) - a % b
# Floor division (//) - a // b
# Exponentiation (**) - a ** b

# Example - Ints
print("Addition: ", 1 + 5)
print("Subtraction: ", 5 - 1)
print("Multiplication: ", 10 * 5)
print("Division: ", 100 /  5)
print("Division without remainder: ", 13 // 5)
print("Modulus: ", 10 % 5)
print("Exponentiation: ", 1 ** 5)

# Example - Floats
print("Floating point numbers: PI" , 3.14)
print("Floating point numbers: Gravity" , 9.81)

# Example - Complex numbers
print("Complex numbers: ", 1 + 3j)
print("Multiplying complex numbers: ", (1 + 1j) * (1 + 2j))

# Comparison Operators
# In programmming, we often compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value.

print(3 > 2)
print( 3 >= 2)
print(3 < 2)
print(3 <= 2)
print( 3 == 2 )
print(3 != 2)
print(len('mango') == len('apple')) # True
print(len('mango') == len('avocado'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))

#comparing something gives either a True or a False
print('True' == 'True: ', True == True)
print('True == False: ', True == False)
print('False == False: ', False == False)

# in addition to the above comparison operator Python uses -
    # is: returns true if both variables are the same object(x is y) 
    # is not: returns true if both variables are not the same object (x is not y)
    # in: returns true if the queried list contains a certain item (x in y)
    # not in: returns true if the queried list have a certain item (x not in y)

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
print('A in Kush', 'A' in 'Kush')
print('B in Kush', 'B' in 'Kush')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2: ', 4 is 2 ** 2)


# Logical Operators
# Unlike other programming languages, Python uses keywords and, or, and notfor logical operators. Logical operators are used to combine conditional statements:

# and - returns true if both statements are true - x < 5 and x < 10
# or - returns true if one of the statements is true - x < 5 or x < 4
# not - reverses the result, returns false if the result is true - not(x < 5 and x < 10)

print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
print(3 < 2 and 4 < 3)
print('True and True:', True and True)
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print( 'True or False:', True or False)
print(not True)
print(not 10 > 5)
print(not False)
print(not not False)
print(not not True)


# Exercises - Day 3

# Declare your age as integer variable
age: int = 2500

# Declare your height as a float variable
height: float = 6.3

# Declare a variable that store a complex number
comp: complex = 5+7j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
heightTri = float(input("Enter your height of triangle: "))
baseTri = float(input("Enter your base of triangle: "))

areaOfTri = 0.5 * baseTri * heightTri
print(areaOfTri)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
sideA = int(input("Enter side A: "))
sideB = int(input("Enter side B: "))
sideC = int(input("Enter side C: "))

perimeterTri = sideA + sideB + sideC
print(perimeterTri)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lengthRect = int(input("Enter length: "))
widthRect = int(input("Enter width: "))

areaRect = lengthRect * widthRect
periRect = 2 * (lengthRect + widthRect)

print(lengthRect)
print(widthRect)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radCirc = int(input("Enter radius: "))
areaCirc = 3.14 * radCirc ** radCirc
circumCirc = 2 * 3.14 * radCirc

print(areaCirc)
print(circumCirc)

# # Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope = 

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)


# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pyLen = len('Python')
drLen = len('Dragon')

print(pyLen)
print(drLen)
print(drLen == pyLen)
# if pyLen == drLen:
#     print('True')
# else:
#     print('False')

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'dragon')

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print('on' not in 'dragon' and 'python')

# Find the length of the text python and convert the value to float and convert it to string
pytLen = len('python')
print(pytLen)
pytLenFlo = float(pytLen)
print(pytLenFlo)
pytLenFloStr = str(pytLenFlo)
print(pytLenFloStr)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
evenNum = int(input("Enter number: "))
if evenNum % 2 == 0:
    print('Even number')
else:
    print('Odd number')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))

#Check if type of '10' is equal to type of 10
print(type(10) == type('10'))

#Check if int('9.8') is equal to 10
print(int(9.8) == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hrs = int(input("Enter hours: "))
rateph = int(input("Enter rate per hour: "))

payCalc = hrs * rateph
print("Week's pay of the employee: ", payCalc)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
yrsLived = int(input("Enter number of years:"))
secInYr = (((60 * 60) * 24) * 365)

secLived = yrsLived * secInYr

print('Number of seconds a person has lived: ', secLived)

# Write a Python script that displays the following table
uno = 1
duo = 2
tres = 3
quatro = 4
pento = 5

print(uno, uno, uno, uno, uno)
print(duo, uno, duo * uno, duo * duo, (duo * duo) * duo)
print(tres, uno, tres * uno, tres * tres, (tres * tres) * tres)
print(quatro, uno, quatro * uno, quatro * quatro, (quatro * quatro) * quatro)
print(pento, uno, pento * uno, pento * pento, (pento * pento) * pento)