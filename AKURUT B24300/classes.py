# Class 1: Animal
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        print("The animal makes a sound.")

# Class 2: Dog
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def sound(self):
        print("The dog barks.")

# Class 3: Cat
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def sound(self):
        print("The cat meows.")

# Class 4: Bird
class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def sound(self):
        print("The bird chirps.")

# Class 5: Fish
class Fish(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def sound(self):
        print("The fish swims silently.")
        
# Create instances of each class
dog = Dog("Fido", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Gray")
bird = Bird("Sunny", 1, "Parrot")
fish = Fish("Goldie", 1, "Aquarium")

# Run the instances
dog.sound()
cat.sound()
bird.sound()
fish.sound()