# Creating the Dog class
class Dog: 
    """A simple attempt to model a dog.
    """
    
    def __init__(self, name, age):
        """Initialize name and age attributes.
        """
        self.name = name
        self.age = age 
        
    def sit(self):
        """Simulate a dog sitting in response to a command
        """
        print(f"{self.name} is now siggint.")
        
    def roll_over(self):
        """Simulate a dog rolling over.
        """

# The __init__() method runs automatically whenever we create a new instance based on the Dog class
# This method has two leading underscores and two trailing undersocores
# This convention helps to prevent Python's default method names from conflicting with your method names
# 
# parameters:
# self parameter:
### - is required in the method definition
### - must come FIRST before the other parameters
### - it must be included in the definition because when Python calls
###       this method automatically pass the self argument.

# 
# Any var prefixed with self is available to every method in the class
# 

# Making an instance from a Class
my_dog = Dog('Wilie', 6)

print(f"My dog's name is {my_dog.name}.")

print(my_dog)