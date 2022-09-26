# for loop
magicians = ['alice', 'david', 'carolina']
for m in magicians:
    print(m)

# Numerical Lists
for i in range(1,5):
    print(i) # prints 1 to 4

# List of numbers
numbers = list(range(1,6))
print(numbers)
for i in numbers:
    print(i)

# Steip Size Generator
even_numbers = list(range(2,11,2))
print(even_numbers)


squares = []
for i in range(1,11):
    square = i ** 2 
    squares.append(square)
print(squares)

# Statistics Functions 
numbers = list(range(100))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# List Comprehensions 
print()
print("List Comprehension")
squares = [value**2 for value in range(11)]
# 1. Open brackets 
# 2. Define the expression for the values to store in the list 
print(squares)

print()
print()
print("-- TRY IT YOURSELF --")
## Try it Yourself
## 1. Use a for loop to print numbers from 1 to 20 inclusive
for value in range(1,21):
    print(value)
## 2. Make a list of the numbers from one to one 100 and print the list
numbers = list(range(1,101))
print(numbers)
## 3. Summing a Million
print(sum(list(range(1,1_000_001))))
## 4. Use 3rd arg in range func to make a list of the odd 1 to 20
print(list(range(0,21,2)))
## 5. use a list comprehension to generate a list of hte first 10 cubes
print([value**2 for value in range(1,11)])

#########################################
#########################################

print()
print()

# Working with part of a list
players = ['charles', 'martin', 'michael', 'fkirence', 'eli']
print(players[0:3])
print(players[:2])
print(players[2:])

# Copying a list 
players_value = players[:]
players_pointer = players 
players_value.append('LeBron')
players.append('Curry')
players_pointer.append('Ginobili')
print(players)
print(players_pointer)
print(players_value)




