# Day 7 - Sets

# Sets are a collectin of items. 
# Maths definition of a set can be applied to python as well.
# Set is a collection of unordered and un-indexed distinct elements. In Python, set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set, and disjoint set among sets.


# Creating a Set
# To create an empty set, we use the set() function. Empty curly brackets {} will create a dictionary - not a set.

# Creating an Empty Set
# syntax 
st = set()

# Creating a set with initial items
# syntax
st = {'item1', 'item2', 'item3', 'item4'}

# example
fruits = {'Apple', 'Banana', 'Ananas', 'Orange'}



# Getting Set's Length
# We use len() method to find the length of a set.
# syntax
len(st)

# example
len(fruits)


# Accessing Items in a Set
# We use loops to access items in a set.

# Checking Items
# To check if an item exists in a set,  we use the in membership operator. 
# syntax
print("Does set st contains item3?", 'item3' in st) # Does set st contain item3? True

# example
print('mango' in fruits) # True


# Adding Items to a Set
# Once a set is created, we cannot change any items and we can also add additional items.

# Add one item using add() method
# syntax 
st.add('item5')

# example
fruits.add('Lime')


# Add multiple items using update()
# The update() allows to add multiple items to a set. The update() takes a list as agrument.
# syntax
st.update(['item6', 'item7', 'item8'])

# example 
veggies = ('Tomato', 'Potato', 'Cabbage', 'Brocolli', 'Onion')
fruits.update([veggies])
print(fruits)


# Removing Items from a Set
# We can remove an item from a set using teh remove() method. If the item is not found, remove() method will raise an error, so it is good to check if the item even exists in the given set. However, discard() method doesnt raise any errors.
# syntax
st.remove('item2')

# The pop() mehtod removes a random item from a list and it returns the removed item.

# example 
removed_item = fruits.pop() # removes a random item from the set and also returns it
print(removed_item) # here, we print the removed item itself


# Clearing Items in a Set
# If we want to clear or empty the set we use clear method.

# syntax
st.clear()

# example 
fruits.clear()
print(fruits) # set() - empty set


# Deleting a Set
# if we want to delete the set itself, we use del operator.

# syntax
del st

# example
del fruits


# Converting List to Set
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.

# syntax
lst = ['item1', 'item2', 'item3']
st = set(lst) # {'item1', 'item2', 'item3'} - the order is random, because sets in general are unordered

# example
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
frut_set = set(fruits)
print(frut_set)


# Joining Sets
# We can join two sets using the union() method or update() method or | symbol.

# Union - This method returns a new set
# syntax
st1 = {'item1', 'item2'}
st2 = {'item3', 'item4'}
st3 = st1.union(st2) #st3 = st1 | st2

# example
frui = {'banana', 'orange', 'mango', 'lemon'}
veggi = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(frui.union(veggi)) # {'potato', 'banana', 'lemon', 'orange', 'carrot', 'onion', 'mango', 'cabbage', 'tomato'}


# Update - This method inserts a set into a given set
# syntax
st4 = {'item1', 'item2'}
st5 = {'item3', 'item4'}
st4.update(st5) # st5 contents are added to st4
print(st4)


# Finding Intersection Items
# Intersection returns a set of items which are in both the sets or using & symbol.

# syntax
st6 = {'item1', 'item2', 'item10', 'item3'}
st7 = {'item10', 'item3', 'item4'}
st6.intersection(st7) # {'item3', 'item10'}

# example
whole_nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_nums = {0, 2, 4, 6, 8, 10}
whole_nums.intersection(even_nums)

pyt = {'p', 'y', 't', 'h', 'o','n'}
dra = {'d', 'r', 'a', 'g', 'o','n'}
pyt.intersection(dra) # {'o', 'n'}


# Checking Subset and Super Set
# A set can be subset or super set of other sets:
#    - Subset - issubset()
#    - Super Set - issuperset()

# syntax
st8 = {'item1', 'item2', 'item10', 'item3'}
st9 = {'item10', 'item3', 'item4'}
st8.issubset(st9) # True
st9.issuperset(st8) # True

# example
whole_nums1 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_nums1 = {0, 2, 4, 6, 8, 10}
whole_nums1.issubset(even_nums1) # False, because it is a super set
even_nums1.issuperset(whole_nums1) # True

pyth = {'p', 'y', 't', 'h', 'o','n'}
dran = {'d', 'r', 'a', 'g', 'o','n'}
pyth.issubset(dran) # False



# Checking the Difference Between Two Sets
# it returns the difference between two sets or using - symbol.

# syntax
st11 = {'item1', 'item2', 'item3', 'item4'}
st12 = {'item2', 'item3'}
st12.difference(st11) # set() : st2 - st1
st11.difference(st12) # {'item1', 'item4'} => st1\st2  : st2 - st1

# example 
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python1 = {'p', 'y', 't', 'o','n'}
dragon1 = {'d', 'r', 'a', 'g', 'o','n'}
python1.difference(dragon1) # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon1.difference(python1) # {'d', 'r', 'a', 'g'}
# dragon1 - python1



# Finding Symmetric Difference Between Two Sets
# It  


# Joining Sets
# If two sets do not have a common item or items, we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

# syntax 
st_new = {'item1', 'item2', 'item3', 'item4'}
st_new2 = {'item2', 'item3'}
st_new2.isdisjoint(st_new) # False - because both dets have items in common

# example 
even_nums_new = {0, 2, 4 ,6, 8}
odd_nums_new = {1, 3, 5, 7, 9}
even_nums_new.isdisjoint(odd_nums_new)  # True - because no common items between the two sets

pyth1 = {'p', 'y', 't', 'h', 'o','n'}
drag1 = {'d', 'r', 'a', 'g', 'o','n'}
pyth1.isdisjoint(drag1) # False - there are items common in both - {'o', 'n'}


# Exercises - Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['OpenAI', 'Meta', 'Microsoft', 'Atlasian'])

# Remove one of the companies from the set it_companies
it_companies.pop()

# What is the difference between remove and discard
# remove - removes an item which you know of from the set. But, if the item is not found, it'll throw an error
# discard - removes the item too, but it doesnt give an error if the item doesnt exist in the set.


# Exercises: Level 2

# Join A and B
C = A.union(B)

# Find A intersection B
A.intersection(B)

# Is A subset of B
A.issubset(B)

# Are A and B disjoint sets
A.isdisjoint(B)

# Join A with B and B with A
A.union(B)
B.union(A)

# What is the symmetric difference between A and B
A.symmetric_difference(B)

# Delete the sets completely
del A
del B


# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(age))
age_st = set(age)
print(len(age_st))

# Explain the difference between the following data types: string, list, tuple and set

# string - is a collection of characters - or more importantly, its words and its denoted between ""
# list - can hold a collection of data, is a data structure - it can hold mixed bag of data - can hold duplicates and can be indexed - denoted by []
# tuples - are also data structures, can be indexed, they are ordered, and do not take duplicates - are denoted by () - cannot be mutated so cannot add or remove data from it unless you change it to somthing else - like a list
# set - are data structures - are random and unindexed - are not indexed so have to use loops to go through them, and they do not take duplicates

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sent = "I am a teacher and I love to inspire and teach people."
lst_sent = sent.split(' ')
print(lst_sent)
print(len(lst_sent))
st_sent = set(lst_sent)
print(len(st_sent))