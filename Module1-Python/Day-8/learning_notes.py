# from abc import ABC, abstractmethod
# class Father(ABC):

# 	@abstractmethod					
# 	def disp(self):					# Abstract Method
# 		pass
		
# #my = Father()						# Not possible to create object of a abstract class

# class Child(Father):
# 	def disp(self):
# 		print("Child Class")
# 		print("Defining Abstract Method")

# class Relative(Father):
# 	def disp(self):
# 		print("Rlative Class")
# 		print("Defining Rlative Method")
# r = Relative()
# c = Child()
# c.disp()

# # Mail ==> Interface
#     # ==> send()  Abstract
# # Email
# # SMS
# # WhatsAPP


# from abc import ABC, abstractmethod

# class Father(ABC):
# 	@abstractmethod
# 	def disp1(self):
# 		pass
# 	@abstractmethod
# 	def disp2(self):
# 		pass

# class Child(Father):
# 	def disp1(self):
# 		print("Child Class")
# 		print("Disp 1 Abstract Method")	


# class GrandChild(Child):
#     def disp2(self):
#         print('Grandchild Class')		
#         print("defined in Grandchild")		
		
# gc = Granchild()
# #gc=Child()
# gc.disp1()
# gc.disp2()


# from abc import ABC, abstractmethod
# from typing import List

# # Step 1: Define Employee interface using Abstract Base Class (ABC)
# class Employee(ABC):
#     @abstractmethod
#     def work(self) -> str:
#         pass
    
#     @abstractmethod
#     def get_salary(self) -> float:
#         pass


# # Step 2: Create concrete classes for different types of employees

# class Manager(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is managing the team."

#     def get_salary(self) -> float:
#         return self.salary


# class Developer(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is writing code."

#     def get_salary(self) -> float:
#         return self.salary


# class Intern(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is learning and assisting."

#     def get_salary(self) -> float:
#         return self.salary


# # Step 3: Define Department class that manages Employees
# class Department:
#     def __init__(self, name: str):
#         self.name = name
#         self.employees: List[Employee] = []

#     def hire(self, employee: Employee) -> None:
#         self.employees.append(employee)
#         print(f"{employee.name} has been hired.")

#     def fire(self, employee: Employee) -> None:
#         self.employees.remove(employee)
#         print(f"{employee.name} has been fired.")

#     def get_total_salary(self) -> float:
#         return sum(employee.get_salary() for employee in self.employees)

#     def show_employee_details(self) -> None:
#         print(f"Employees in {self.name} Department:")
#         for employee in self.employees:
#             print(f"- {employee.name}, Salary: {employee.get_salary()}, Role: {employee.work()}")

# class Security(Employee):
#     def __init__(self, name: str, salary: float):
#         self.name = name
#         self.salary = salary

#     def work(self) -> str:
#         return f"{self.name} is Securing the assets."

#     def get_salary(self) -> float:
#         return self.salary
    
# # Step 4: Create department and add employees

# # Create employees
# manager = Manager("Alice", 80000)
# developer = Developer("Bob", 60000)
# intern = Intern("Charlie", 20000)
# securitystaff=Security("Ram",5000)

# # Create a department and hire employees
# it_department = Department("IT")

# it_department.hire(manager)
# it_department.hire(developer)
# it_department.hire(intern)
# it_department.hire(securitystaff)
# # Show employee details
# it_department.show_employee_details()

# # Total salary in the department
# total_salary = it_department.get_total_salary()
# print(f"Total salary expense for {it_department.name} department: ${total_salary}")


# from abc import ABC, abstractmethod

# # Abstract class
# class Animal(ABC):
    
#     @abstractmethod
#     def make_sound(self):
#         """Abstract method with no implementation"""
#         pass

# # Child class implementing the abstract method
# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"



# class Cat(Animal):
#     def make_soundS(self):
#         return "Bark"
    
# # Creating an instance of Dog
# dog = Dog()
# cat=Cat()
# print(dog.make_sound())  # Output: Bark


# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def max_speed(self):
#         pass

#     def start_engine(self):
#         return "Engine started."

# class Car(Vehicle):
#     def max_speed(self):
#         return '200'

# class Bike(Vehicle):
#     def max_speed(self):
#         return '100'
# bik=Bike()
# car = Car()

# def drive(obj):
#     class_str =str(type(obj))
#     vehicle_name = class_str.split('.')[-1].split('>')[0] 
#     vehicle_name+= obj.start_engine();   
#     print(vehicle_name)
#     vehicle_speed =vehicle_name 
#     vehicle_speed+=obj.max_speed()
#     print(vehicle_speed)
    
# drive(bik)
# drive(car)