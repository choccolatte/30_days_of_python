# Day 8 - Dictionaries

# A dictionary is a collection of unordered, modifiable (mutable) paired (key: value) data type.


# Creating a Dictionary
# To create a dictionary, we use the curly braces, {} or dict() - the built-in function.

# syntax 
empty_dict = {}
# Dicionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# example
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# the dictionary above shows that a value could be any data type - string, boolean, list, tuple, set or dictionary.


# Dictionary Length
# It checks the number of key:value pairs in the ddictionary.

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

# example
person_new = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(len(person_new)) # 7


# Accessing Dictionary items
# We can access dictionary items by referring to by its key's name to get the value.

# syntax
dct_accs = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct_accs['key1']) # value1
print(dct_accs['key4']) # value4

# example
person_accs = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(person_accs['first_name'])
print(person_accs['age'])
print(person_accs['skills'])
print(person_accs['address'])
# print(person_accs['city']) # error

# accessing an item by its key name raises an error if the key does not exist. To avoid this error, first we need to check if a key exists or we can use the get method. The get method returns None, which is a NoneType object data type, if the key does not exist.

print(person_accs.get('skills'))
print(person_accs.get('address'))
print(person_accs.get('city'))


# Adding Items to a Dictionary
# We can add new key and value pairs to a dictionary.

# syntax
dct_add = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_add['key5'] = 'value5'

# example
person_accs['city'] = 'Vancouver'
person_accs['job_title'] = 'Software Engineer'
person_accs['skills'].append('Java') # this because skills was a list, and we're appending to a list
print(person_accs)


# Modifying Items in a Dictionary
# We can modify items in a dictionary.

# syntax
dct_mod = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_mod['key1'] = 'value-one'

# example
person_accs['first_name'] = 'Kush'
person_accs['last_name'] = 'Sin'
person_accs['age'] = 2500
print(person_accs)


# Checking Keys in a Dictionary
# We use the in operator to check if a key exists in a dictionary.

# syntax
dct_chck = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct_mod) # True
print('key5' in dct_mod) # False


# Removing Key and Value Pairs from a Dictionary
# pop(key) - removes the item with the specified key name
# popitem() - removes the last item
# del - removes an item with the specified key name - can also be used to deelte the entire dictionary

# syntax
dct_rem = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_mod.pop('key1') # removes key1:value1
dct_mod.popitem() # removes last item - key4:value4
del dct_mod['key2'] # removes key2:value2

# example
person_del = person_accs.copy()
person_del.pop('first_name')
person_del.popitem()
del person_del['city']
print(person_del)


# Changing Dictionary to a List of Items
# The items() method changes dictionaruy to a list of tuples.

# syntax 
dct_chge = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct_chge.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

print(person_accs.items())

# Clearing a Dictionary
# If we do not want the dictionary, we can clear them using the clear() method using the clear() method.

# syntax 
dct_clr = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct_clr.clear()) # none


# Deleting a Dictionary
# If we do not use the dictionary, we can delete it completely using the del keyword followed by the dictionary's name.

# syntax
dct_del = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct_del


# Copy a Dictionary
# We can copy a dictionary using the copy() method. Using the copy() method, we can avoid mutation of the original dictionary - basically creates a copy of the original dict.

# syntax
dct_cpy = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_cpy_cpy = dct_cpy.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


# Getting Dictionary Keys as a List
# The keys() method gives us all the keys of a dictionary as a list.

# syntax
dct_key = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct_key.keys()
print(keys) #dict_keys(['key1', 'key2', 'key3', 'key4'])


# Getting Dictionary Values as a List
# The values() method gives you all the values of a dictionary as a list.

# syntax
dct_val = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct_val.values()
print(values) # dict_values(['value1', 'value2', 'value3', 'value4'])


# Exercises - Day 8

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Max'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 2
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Kush',
    'last_name': 'Sin',
    'gender': 'Male',
    'age' : 15,
    'marital_status': 'Not Married',
    'skills': ['Programming', 'Writing', 'Sales', 'Project Management'],
    'country': 'Canada',
    'city': 'Vancouver',
    'address': {'Street 5', 'House 36', 'Vancouver'}
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('Computer Science')
student['skills'].append('Leadership')
print(student)

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

# Delete one of the items in the dictionary
student.pop('city')

# Delete one of the dictionaries
del dog
# print(dog) # error