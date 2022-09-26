cars = ['audi', 'toyota', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

## Check Equiality
cars = ['audi', 'toyota', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print( f"{car.upper()} {car=='bmw'}")
    else:
        print( f"{car.title()} {car=='bmw'}")


# Testing for equality is case sensitive in Python
car = 'Audi'
print(car=='audi')
print(car.lower()=='audi')

# inequality
print(car != 'audi')


## Checking Whether a Value Is in a List 
print()
print()
print('Using Lists')
requested_users = 'christian93', 'hugo34', 'monster19'
print('kath3030' in requested_users)
print('hugo34' in requested_users)
print('hugo34' not in requested_users)

# Booleans 
game_active = True
can_edit = False 

# If,Elsif,Else
age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admision cost is $25")
else:
    print("Your admission cost is $40")

print()
print()

# multiple elif
age = 12

if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admision cost is $25")
elif age < 65:
    print("your admission cost is $40")
else:
    print("Your admission cost is $20")
    

print()
print()
# Checking that a list is not empty

requested_toppings = []
if requested_toppings:
        for requested_topping in requested_toppings:
            print(f"Adding {requested_topping}")
else:
    print("Are you sure you want a plain pizza?")


print()
print()
# using multile lists 
available_toppings = [  'mushrooms', 'olives', 'green peppers', 
                        'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = [  'mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("finished Making your pizza!")
