# Day 5 - Lists

# There are 4 different collection of data types in python -

# List - is a collection which is ordered and unchangable(modifiable). It allows duplicate members.

# Tuple - is a collection which is ordered and unchangable or unmodifiable(immutable). It allows duplicate members.

# Set - is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.

# Dictionary - is a collection which is unordered, changable(modifiable) and indexed. No duplicate members allowed.

# A list is a collection of different data types which is ordered and modifiable (mutable). A list can be empty or it may have different data type items.

# How to Create a List?
# In Python, we can create lists in two ways -
#    - Using list built-in function
#   syntax - lst = list()

empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

# using square brackets, []
# syntax - lst = []

empty_list2 = [] # this is an empty list, no item in the list 
print(len(empty_list2)) # 0

# Lists with initial values. We use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']
veggies = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_prods = ['milk', 'meat', 'butter', 'yoghurt']
web_tech = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['India', 'USA', 'Australia', 'England', 'China', 'Japan']

# print the list and its lengths
print('fruits:', fruits)
print(len(fruits))
print('veggies:', veggies)
print(len(veggies))
print('animal_products:', animal_prods)
print(len(animal_prods))
print('web technologies:', web_tech)
print(len(web_tech))
print('countries:', countries)
print(len(countries))


# Lists can have items of different data types too
lst_new = ['Kush', 2500, True, {'country': 'Canada', 'city': 'Vancouver'}]


# Accessing List Items using Positive Indexing
# We access each item in a list using their index. A list index starts from 0.
first_fruit = fruits[0] # 
sec_country = countries[1] #
last_tech = web_tech[-1] # 


# Accessing List items Using Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
alst_fruit = fruits[-1]
last_count = countries[-1]
sec_last_tech = web_tech[-2]


# Unpacking List Items
lst_new2 = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, sec_item, third_item, *rest = lst_new2
print(first_item)
print(sec_item)
print(third_item)
print(rest) # ['item4', 'item5']


# slicing Items from a List
# Positive Indexing - we can specify a range of positive indexes by speciffying the start, end and step, the return value will be a new list. (default values for start = 0, end = len(list) - 1 (last item), step = 1)

fruits_new = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits_new[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits_new[0:] # if we dont set where to stop, it will take all the rest


# Negative indexing - we can also specify a range of negative indexes by specifying the start, end adn step, the return value will be a new list.
all_fruits_rev = fruits_new[-4:] # it returns all the fruits
orange_and_mango = fruits_new[-3: -1] # it does not include the last index ['orange', 'mango']
orange_mango_lemon = fruits_new[-3:] # this will give starting from -3 to the end, ['orange', 'mango', 'lemon']
reverse_fruits = fruits_new[::-1] # a negative step will take the list in reverse order ['lemon', 'mango', 'orange', 'banana']


# Modifying Lists
# List is a mutable or modifiable ordered collection of items. Lets modify the fruits list.
fruits_new2 = ['banana', 'orange', 'mango', 'lemon']
fruits_new2[0] = 'avocado' # changes the first item to avocado
print(fruits_new2) #['avocado', 'orange', 'mango', 'lemon']
fruits_new2[1] = 'apple' # changes 2nd item to apple
last_index = len(fruits_new2) - 1
fruits_new2[last_index] = 'lime' # changes last item to lime
print(fruits_new2) 


# Checking items in a list
# Checking an item if it is a member of a list using the in operator. See example below -
does_exist_in_fruits_new2 = 'banana' in fruits_new2
print(does_exist_in_fruits_new2) # True
does_exist = 'lemon' in fruits_new2
print(does_exist) # False


# Adding Items to a List
# To add items to the end of an existing list, we use the method append().

# syntax
# lst2 = list()
# lst2.append(item)

fruits_new2.append('Cherry')
print(fruits_new2)
fruits_new2.append('Ananas')
print(fruits_new2)


# Inserting Items into a List
# We can use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right. The insert() method takes two arguments - index and an item to insert.

# # syntax
# lst_new = ['item', 'item2']
# lst_new.insert(index, item)

fruits_new2.insert(2, 'Dragon Fruit')
print(fruits_new2)
fruits_new2.insert(-1, 'Tomato')
print(fruits_new2)


# Removing Items from a List
# THe remove method removes a specified item from a list.

# syntax
# lst = ['item', 'item2']
# lst.remove(item)

fruits_new2.remove('Tomato')
print(fruits_new2)


# Removing Items Using Pop()
# The pop() method removes the specified index, (or at last item if index is not specified).

# syntax
# lst = ['item', 'item2']
# lst.pop() # removes last index item
# lst.pop(index) # removes indexed item

fruits_new2.pop()
print(fruits_new2)

fruits_new2.pop(0)
print(fruits_new2)


# Removing Items using Del
# The Del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely.

# syntax
# lst = ['item', 'item2']
# del lst[index] # removes the indexed item
# del lst # removes entire list entirely

del fruits_new2[0] # removes 1st item
print(fruits_new2)
del fruits_new2
# print(fruits_new2) # gives errorr


# Clearing List Items
# The clear() method empties the list of all of its items

# syntax
# lst = ['item', 'item2']
# lst.clear()

fruits_new.clear()
print(fruits_new) # []


# Copying a List
# It is possible to copy a list by reassigning it to a new variable in the following way - list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original list1. But there are lots of cases in which we do not like to modify the original instead we like to have a different copy. One of way of avoiding the problem above is using copy().

# syntax 
# lst = ['item1', 'item2']
# lst_copy = lst.copy()

fruits_new2 = ['avocado', 'apple', 'Dragon Fruit', 'mango', 'lime', 'Cherry', 'Ananas']
fruits_new3 =fruits_new2.copy()
print(fruits_new2)
print(fruits_new3)


# Joining Lists
# There are several ways to join a list, or concatenate, two or more list in Python.

# Plus Operator (+)
# syntax 
# list3 = list1 + list2

pos_nums = [1,2, 3, 4, 5]
zero = [0]
neg_nums = [-3, -2, -1]
ints = neg_nums + zero + pos_nums
print(ints)

# Joining using extend() method - the extend() method allows to append list in a list. 

# syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4']
# list1.extend(list2)

pos_nums1 = [1,2, 3, 4, 5]
neg_nums1 = [-3, -2, -1]
neg_nums1.extend(pos_nums1)
print(neg_nums1)


# Counting Items in a List
# The count() method returns the number of item appears in a list:

# syntax 
# lst = ['item1', 'item2']
# lst.count(item)

fruits_new4 = fruits_new2.copy()
print(fruits_new4)
fruits_new4.append('mango')
print(fruits_new4.count('mango')) # 2


# FInding Index of an Item
# The index() method returns the index of an item in the list.

# syntax
# lst = ['item1', 'item2']
# lst.index(item1)

print(fruits_new4.index('mango'))
ages = [44, 55, 34, 23, 12, 65, 78]
print(ages.index(23))


# Reversing a List
# The reverse() method reverses the order of a list.

# syntax
# lst = ['item1', 'item2']
# lst.reverse()

fruits_new4.reverse()
print(fruits_new4)


# Sorting List Items
# To sort lists, we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in an ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.

# - sort() - this method modigies the original list
# syntax
# lst = ['item1', 'item2']
# lst.sort() # in ascending order
# lst.sort(reverse = True) # in descending order

fruits_new5 = fruits_new4.copy()
fruits_new5.sort()
print(fruits_new5)
fruits_new5.sort(reverse=True)
print(fruits_new5)

# - sorted - returns the ordered list without modifying the original list

print(sorted(fruits_new5)) # ascending 
print(sorted(fruits_new5, reverse=True)) # descending 


# Exercises - Day 5

# Exercises: Level 1

# Declare an empty list
emp_lst = list()

# Declare a list with more than 5 items
ful_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find the length of your list
print(len(ful_lst))

# Get the first item, the middle item and the last item of the list
print(ful_lst[0])
print(ful_lst[-1])
print(ful_lst[4])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Kush', 2500, 178, 'single', 'Canada']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[4])
print(it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'Apple'
print(it_companies)

# Add an IT company to it_companies
it_companies.insert(0, 'Tesla')

# Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Atlassian')

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0].capitalize()

# Join the it_companies with a string '#;  '
str_has = '#'
it_companies.extend(str_has)
print(it_companies)

# Check if a certain company exists in the it_companies list.
print('SpaceX' in it_companies)

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.reverse()

# Slice out the first 3 companies from the list
f_three = it_companies[0:3]

# Slice out the last 3 companies from the list
l_three = it_companies[-4:-1]

# Slice out the middle IT company or companies from the list
m_three = it_companies[3:6]

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(5)

# Remove the last IT company from the list
it_companies.pop()

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')


# Exercises: Level 2

# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
print(min)
max = ages[-1]
print(max)

# Add the min age and the max age again to the list
ages[0] = 19
ages[1] = 26

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(len(ages))
median_age = ages[5] + ages[6] / 2
print(median_age)

# Find the average age (sum of all items divided by their total )
total_ages = sum(ages)
avg_age = total_ages/len(ages)
print(avg_age)

# Find the range of the ages (max minus min)
min_new = ages[0]
max_new = ages[-1]
range_ages = max_new-min_new
print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method
val1 = min_new - avg_age 
print(val1)
val2 = max_new - avg_age
print(val2)
cmpr = val2 - val1
print(abs(cmpr))

# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
print(len(countries)/2 - 1)
print(countries[96])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(len(countries))
first_half = countries[0:96]
first_half[0] = 'India'
sec_half = countries[97:]
print(first_half)
print(sec_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
new_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
c1, c2, c3, *scandic_countries = new_countries
print(c1)
print(c2)
print(c3)
print(scandic_countries)