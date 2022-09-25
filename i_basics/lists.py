# Lists
#
# A list is a collection of items in a particular order
# Square brackets indicated a list 
my_list = ['hello', 'world', 'from', 'list']
my_empty_list = []
print(my_list)

# Accessing Elements 
print(my_list[0])
print(my_list[-1])

# Individual Values
names = ['oscar', 'norbert']
message = f"My name is {names[0].title()}."
print(message)

# Change, Adding and Removing Elements in a List 
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

print("\nChanging:")
motorcycles[0] = 'ducati'
print(motorcycles)

print("\nAdding:")

# Append: add to the end of the list 
print("Appending")
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

print("Inserting to pos 2 ")
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(2, 'ducati')
print(motorcycles)

print()
print("Removing")
motorcycles = ['honda','yamaha','suzuki']
print("By value 'honda'")
motorcycles.remove('honda')
print(motorcycles)

print("By index (using del statement)")
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)

print("Removing using pop() method: lets you work with that item after removing it")
motorcycles = ['honda','yamaha','suzuki']
popped_motorcycle = motorcycles.pop()
print(f"Popped Motorcycle: {popped_motorcycle}")
print(motorcycles)

print("Removing using pop(1)")
motorcycles = ['honda','yamaha','suzuki']
popped_motorcycle = motorcycles.pop(1)
print(f"Popped Motorcycle: {popped_motorcycle}")
print(motorcycles)

## SORTING
print()
print()
print("ORGANIZING A LIST\n")

cars = ['bmw', 'audi', 'toyota', 'subaru', 'chevrolet', 'ford', 'volkswagen']
print(cars)
print("Sorting...")
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting Temporarily
print()
cars = ['bmw', 'audi', 'toyota', 'subaru', 'chevrolet', 'ford', 'volkswagen']
print(cars)
print("temporarily sorted: sorted() function")
print(sorted(cars))

print("get the Length")
print(len(cars))


