print("hello world!")

# data types

# list - is an ordered collection whcih allows to store different data type items. A list is similar to an array in JS.
# eg. - [0, 1, 2, 3, 4, 5], ["Mango", "Banana", Berry], [1, "Mango", 2, "Berry"]

# Dictionary - a python dict object is an unordered collection of data in a key value pair format.
# eg. - {'first': 2, 'sec':2, 'third':3, 'more':[1, 2, 3, 4, 5]}

# tuple - a tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
# eg. - ('first', 'sec', 'third')

# Set - a set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Maths, sets in python stores only unique items.
# eg. - {2, 3, 4, 5, 6}

# type() function

# day 1
# python3 --version



# Euclidean distance of - (2, 3) and (10, 8)

#horizontal diff
diff = 2 - 3
print(diff)

#vertical diff
vdiff = 10 - 8
print(vdiff)

# square both
diffSqr = diff * diff
vdiffSqr = vdiff * vdiff

# add squares
newSqr = diffSqr + vdiffSqr

# take square root - exponentiation with 0.5
res = newSqr ** 0.5
print(res)