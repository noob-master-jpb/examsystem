# Base class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name


# Subclass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball"


# Subclass
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

    def scratch(self):
        return f"{self.name} is scratching"


# Creating instances of the subclasses
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")
a = Animal("jo")
# Using methods from the base class
print(a.speak())

