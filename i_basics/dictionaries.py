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

# Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key,value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    
print()
print()

# Looping through all the keys
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'ruby',
    'monica': 'python',
    'carlos': 'c'
}

for name in fav_languages.keys():
    print(name.title())
print()
for language in fav_languages.values():
    print(language.title())
print()

# the set() function builds a set for unique languages in the list
print("The following languages have been mentioned:")
for language in set(fav_languages.values()):
    print(f"\t{language}")
    
print()
# Looping in order
for name in sorted(fav_languages.keys()):
    print(f"{name.title()}, Thank you for takign the poll.")

print()
print()

# Nesting: multiple dictioneries in a list
print("Nesting")
# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
# change aliens characteristics 
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:6]:
    print(alien)
print()
print()

######################### 
# A list in a dictionary 
######################### 

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza" 
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
print()
