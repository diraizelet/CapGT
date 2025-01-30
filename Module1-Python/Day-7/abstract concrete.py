from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Concrete class
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()  
cat.make_sound()

dog.sleep()  
cat.sleep()