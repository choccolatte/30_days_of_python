# Python Date 

# Python has got datetime module to handle date and time. The datetime module has got a class called datetime which allows us to work with date and time.

import datetime
print(dir(datetime)) # prints all the attributes and methods of the datetime module
# ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

# With dir or help built-in commands, its possible to know the available functions in a certain module. As you can see, in the datetime module, there are many functions, but we will right now focus on date, datetime, time and timedelta. Lets now see them one by one -


# Getting datetime information
# The datetime module has got a class called datetime which allows us to work with date and time

from datetime import datetime
now = datetime.now() # current date and time
print(now) # 2026-08-05 23:33:50.429892

day = now.day # current day
month = now.month # current month
year = now.year # current year
hour = now.hour # current hour
minute = now.minute # current minute
second = now.second # current second
timestamp = now.timestamp() # current timestamp
print(day, month, year, hour, minute, second, timestamp) # 5 8 2026 23 33 50 1728239630.429892
print(f'current timestamp: {timestamp}') # current timestamp: 1728239630.429892
print(f'{day}/{month}/{year} {hour}:{minute}:{second}') # 5/8/2026 23:33:50

# Timestamp or Unix timestamp is the number of seconds since 1 January  UTC. It is a way to represent a point in time as a single number. The timestamp can be converted to a datetime object using the fromtimestamp() method of the datetime class.
# The fromtimestamp() method takes a timestamp as a parameter and returns a datetime object.


# Formatting Date Output Using strftime
from datetime import datetime
new_year = datetime(2026, 1, 1)
print(new_year) # 2026-01-01 00:00:00 - default format is YYYY-MM-DD HH:MM:SS
# We can format the date output using strftime() method. 
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute, second) # 1 1 2026 0 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}') # 1/1/2026, 0:0:0


# Formatting Date Output Using strftime method and its documentation can be found on this link - https://www.bairesdev.com/tools/strftime/

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S") # current time
print("time:", t) # time: 23:33:50
# print(dir(datetime)) # prints all the attributes and methods of the datetime module

time_one = now.strftime("%m/%d/%Y, %H:%M:%S") # current date and time
# mm/dd/yyyy, HH:MM:SS format
print('time_one:', time_one) # time_one: 08/05/2026, 23:33:50
time_two = now.strftime("%d/%m/%Y, %H:%M:$S") # current date and time
# dd/mm/yyyy, HH:MM:SS format
print('time_two:', time_two) # time_two: 05/08/2026


# String to Time Using strptime




#The strftime() method takes a format string as a parameter and returns a string representing the date in the specified format. The format string can contain various format codes that represent different parts of the date and time. For example, %Y represents the year with century as a decimal number, %m represents the month as a zero-padded decimal number, %d represents the day of the month as a zero-padded decimal number, %H represents the hour (24-hour clock) as a zero-padded decimal number, %M represents the minute as a zero-padded decimal number, and %S represents the second as a zero-padded decimal number. There are many other format codes available in the strftime() method.