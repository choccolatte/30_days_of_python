# Day 6 - Tuples

# A tuple is a collection of different data types which is ordered and unchangable (immutable). Tuples are written with round brackets(). Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). Unlike lists, tuples have few methods. Methods related to tuples are -
#   - tuple() - to create an empty tuple
#   - count() - to count the number of a specified item in a tuple
#   - index() - to find the index of a specified item in a tuple
#   - + operator - to join two or more tuples and to create a new typle


# Creating a Tuple
# Empty tuple: Creating an empty tuple

# syntax 
# empty_tuple = ()
# or using the tuple constructor
# empty_tuple = tuple()

# tuples with initial values
# syntax 
tpl = ('item1', 'item2', 'item3')

fruits = ('Banana', 'Apple', 'Ananas')

# Tuple length
# We use the len() method to get the length of a tuple as well.
# syntax
len(tpl) # 3


# Accessing Tuple Items
# Positive indexing - similar to the list data type we use positive or negative indexing to access tuple items - starts from 0, goes till n
# syntax
f_item = tpl[0]
sec_item = tpl[1]
las_item = tpl[-1]

f_frut = fruits[0]
sec_frut = fruits[1]
las_frut_index = len(fruits) - 1
las_frut = fruits[las_frut_index]


# Negative INdexing - means beginning from the end towards the start. -1 refers to the last item, -2 refers to the second last item, and the negative of the list/tuple length(entire length of the tuple/list) refers to the first item.
# synax 
f_item_rev = tpl[-1]
sec_item_rev = tpl[-2]

f_frut_rev = fruits[-(len(fruits))]
print(f_frut_rev)
l_frut_rev = fruits[-1]
print(l_frut_rev)


# Slicing Tuples
# We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

# Range of Positive Indexes
# syntax
al_items = tpl[0:]  # gives all items
lst_two_item = tpl[1:] # will not include item at the second number in the numerical ratio

frut_all = fruits[0:]
print(fruits)
ban_apl = fruits[:2] # first two items
print(ban_apl)
apl_anan = fruits[1:] # last two items
print(apl_anan)


# Range of Negative Indexes
# syntax
al_tpl_items = tpl[-4:] # all items 
mid_two_items = tpl[-3:-1] # does not include item at index -3

al_fruts = fruits[-4:]
print(al_fruts)


# Changing Tuples to Lists
# We can change tuples to lists and lists to tuples. Tuple is immutable if we want to modify a tuple we should change it into a list first, else it'll throw an error
# syntax
lst_of_tpl = list(tpl)

fruits_list = ('banana', 'orange', 'mango', 'lemon')
fruits_list = list(fruits_list)
print(fruits_list)
fruits_list[0] = "Strawberry"
print(fruits_list)
fruits_list = tuple(fruits_list)
print(fruits_list)


# Checking an Item in a Tuple
# We can check if an item exists or not in a tuple using in, it returns a Boolean.
# synax 
tpl_new = ('item1', 'item2', 'item3','item4')
'item5' in tpl_new # False

print('Apple' in fruits_list) # False
print('Strawberry' in fruits_list) # True


# Joining Tuples
# We can also join two or more tuples using the + operator
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item3', 'item4', 'item6')
tpl3 = tpl1 + tpl2

veggies = ('Tomato', 'Potato', 'Cabbage', 'Brocolli', 'Onion')
fruits_and_veggies = fruits_list + veggies
print(fruits_and_veggies)


# Deleting Tuples
# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del. Or, you can convert the tuple into a list, delete hte item from the list, then convert the list back to a tuple - like we did when we added an item to the tuple(list)
# syntax
del tpl1

del fruits_list
# print(fruits_list) # error coz deleted




# 💻 Exercises: Day 6


# Exercises: Level 1

# Create an empty tuple
emp_tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
bros = ('Kriss', 'John', 'Alec')
sis = ('Leona', 'Larissa')

# Join brothers and sisters tuples and assign it to siblings
siblings = bros + sis

# How many siblings do you have?
print(len(siblings)) # 5

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members[0] = 'Kush'
family_members[1] = 'Wu'
family_members = tuple(family_members)
print(family_members)


# Exercises: Level 2
# Unpack siblings and parents from family_members
father, mother, *siblings2 = family_members

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruts = ('Carrot', 'Apple', 'Ananas', 'Cherry', 'Guava', 'Mango')
vegg = ('Potato', 'Tomoto', 'Cabbage', 'Brocolli')
anml_prods = ('Chicken', 'Pork', 'Fish', 'Eggs')
food_stuff_tp = fruts + vegg + anml_prods
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt[8:9]

# Slice out the first three items and the last three items from food_stuff_lt list
food_stuff_lt[:3]
food_stuff_lt[-3:-1]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)