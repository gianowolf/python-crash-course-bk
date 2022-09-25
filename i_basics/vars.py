# Variables
#   [0-9] [A-Z] [a-z] and '_'
#
# Data Types
#
# # Strings 
# # "this is a string", 'this is also a string'

name = "ada lovelace"
# variable.method() 
print(name.title()) # Ada Lovelace 
print(name.upper()) # ADA LOVELACE
print(name.lower()) # ada lovelace 

# Variables in Strings
## letter f immediately before the opening quotation mark
## These are calling f-strings (format strings)
def newl():
    print("\n")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

newl()
message = (f"Hello, {full_name.title()}")
print(message)
print(message.rstrip())

## Multiple Assignment
x, y, z, = 0, 0, 0

## Constants 
# ! PYTHON DOESN'T HAVE BUILT-IN CONSTANT TYPES
# ? Python Programmers uses all-capital letters 
MAX_CONNECTIONS = 5000