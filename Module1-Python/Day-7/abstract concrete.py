from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

#     def sleep(self):
#         print("This animal is sleeping")

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# # Concrete class
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# dog = Dog()
# cat = Cat()

# dog.make_sound()  
# cat.make_sound()

# dog.sleep()  
# cat.sleep()


# class interfacereading:
#     def __init__(self):
#         pass
#     def trial(self):
#         pass
#     def trail(self):
#         pass

# from abc import ABC, abstractmethod

# class vehicle:
#     def __init__(self):
#         self.__brand_name ="Yamaha"
#     def max_speed(self):
#         pass

# class Car(vehicle):        
#     @abstractmethod
#     def max_speed(self):
#         return "200 km/h"

# class Bike(vehicle):
#     def max_speed(self):
#         return "150km/h"

# car_obj=Car()

# print("The max speed of the car is ",car_obj._vehicle__brand_name)


#using abstract class method in derived class
# class shape:
#     def __init__(self):
#         pass

#     def area(self):
#         pass

# class rectangle(shape):
#     def __init__(self,length,breadth):
#         self.__length=length
#         self.__breadth=breadth

#     def area(self):
#         return self.__length*self.__breadth
# class circle(shape):
#     def __init__(self, radius):
#         self.__radius=radius
#     def area(self):
#         return 3.14 * (self.__radius*2)


# calling the abstract method from parent class
# class father:
#     @abstractmethod
#     def profession(self):
#         pass
#     def introduce(self):
#         self.profession()

# class doctor(father):
#     def profession(self):
#         print("this is the profession method in the doctor class.")

# class engineer(father):
#     def profession(self):
#         print("this is the engineer class.")


# doc_obj = doctor()
# eng_obj =engineer()
# doc_obj.introduce()
# eng_obj.introduce()


#multiple inheritance with abstract class
# class person:
#     def __init__(self,name):
#         self.__name=name
#     @abstractmethod
#     def get_name(self):
#         pass

# class employee:
#     @abstractmethod
#     def get_salary(self):
#         pass


# class manager(person,employee):
#     def get_name(self):
#         print("The name is ::")
#     def get_salary(self):
#         print("The salary is ::")

# man_obj=manager("Ron")
# man_obj.get_name()
# man_obj.get_salary()