# Functions
def greet_user(user):
    """Display a simple greeting.""" # docstring: describes what the function does
    print(f"Hello, {user.title()}!")
    
greet_user("javi")

# dog is a default value
def describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type.lower()} called {pet_name.title()}")

# Positional call
describe_pet("dog","firulais")
# Keyword call
describe_pet(pet_name="luna",animal_type="cat")

# Passing a List
# The function gets direct access to the contents of the list 
# The function can modify the list 
    # function_name(list_name)
# To prevent a function from modifying a list:
# The slice notation [:] makes a copy of the list 
    # function_name(list_name[:])

print()

# Passing arbitrary number of arguments 
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Arbitrary keyword arguments 
# write a function that accept as may key-value pairs as the calling statement provides
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info 

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

# The function expected a first and a last name
# then it allows the user to pass in as many name-value pairs as they want
# The ** beofre the parameter cause PYthon to create an empty dictionary called user_info 
# and pack whatever name-value pairs it receives into this dictionary

