# Dictionaries 
# Allows you to connect pieces of related information

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# A dictionary in Python is a collection of key-value pairs
# each key is connected to a value 
# you can use a key to access the value associated with
# a key's value can be a number, a string, a list, or even another dictionary

# Dictionaries are wrapped in braces {}
# 

# Adding New Key-Value Pairs
alien_0['x_position']= 0
alien_0['y_position']= 25
print(alien_0)

# Modifying Values in a dictionary
alien_0['color'] = 'red'
print(alien_0)

# Removing Key-Value Pairs 
del alien_0['points']
print(alien_0)

# Using get() method
# Square Brackets causes a error if the key does not exist
# get() method requires a key as a first argument
# As a optional second argument, you can pass the value to be returned if the key does not exist
print(alien_0.get('age','no age assigned'))


