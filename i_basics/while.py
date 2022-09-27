# while loops

current_number = 1 
while current_number <= 5:
    print(current_number)
    current_number += 1

# Break
prompt = "\nPlease enter the name of a city you have visited"
prompt += "\n(Enter 'quit' when you are finished.)"
cities = []

print(prompt)
while True:
    city = input()
    if city == 'quit':
        break
    else: 
        cities.append(city)

for city in cities:
    print(city.title())

print()
print()

# Using A WHILE LOOP WITH LISTS AND DICTIONARIES 

# One way whould be to use a while loop to pull from the list
# of unconfirmed users 

unformirmed_users = [ 'alice', 'brian', 'candance']
confirmed_users = []

# THE WHILE LOOP RUNS ALONG AS HET LIST IS NOT EMPTY
while unformirmed_users:
    current_user = unformirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# Removing all instances
from random import seed 
from random import randint

nums = []
count = 0;
target = int(input("Ingrese un numero a borrar:"))
seed(1)

for i in range(100000):
    nums.append(randint(1, 100))

while target in nums:
    nums.remove(target)
    count +=1
print(f"removed {count} '{target}'")
