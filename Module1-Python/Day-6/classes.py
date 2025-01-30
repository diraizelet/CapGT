# class car:
#     def __init__(self,name):
#         self.brand=name
    
# class Skoda(car):
#     def setWheels(self,wheel):
#         self.wheelSize=wheel
#     def setDoors(self,doors):
#         self.countDoor=doors
#     def setEngine(self, engine):
#         self.engineType=engine
    
# if __name__ =="__main__":
#     s = Skoda("Skoda")
#     s.setDoors("Double Doors")
#     s.setEngine("V4")
#     s.setWheels(84) 
#     print(s.brand+" "+s.countDoor+" "+s.engineType)

class worker:
    def __init__(self,level):
        self.level=level
        

# class employee(worker):
#     def __init__(self, designation):
#         self.designation=designation
#     def paid_salary(self,salary):
#         self.salary=salary
#     def Work_timings(self,timings):
#         self.timings=timings
    
#     def late_count(self):
#         self.late+=1
#     def department(self,dept):
#         self.department=dept


# class employee(worker):
#     def __init__(self):
#         super().__init__()
#     def set_name(self,name):
#         self.__name=name
#     def set_salary(self,salary):
#         if salary>0:
#             self.__salary=salary
#     def get_salary(self):
#         if self.__name!="":
#             return self.__salary
#     def get_allowances(self,allowances):
#         self.__salary=self.__salary+sum(allowances)
#         return self.__salary
#     def get_deductions(self, deductions):
#         for i in deductions:
#             subst=(i*self.__salary)/100
#             self.__salary= self.__salary-subst
#             return self.__salary

# def main():
#     employee1=employee(int(input("enter the level of the employee:")))
#     employee1.set_salary(int(input("Enter the salary: ")))
#     print("The total salary with food and travel expenses: ",employee1.get_allowances([2000,3000]))
#     print("The salary after all deductions is: ",employee1.get_deductions([18,21]))

# main()

# class Educational_institution:
#     def __init__(self):
#         print("Created a institution.")
    
#     def Teachers(self):
#         print("There are teachers.")
    
#     def Students(self):
#         print("There are students.")
    

#     def no_of_classes(self):
#         print("There are classrooms.")


# class School(Educational_institution):

#     def __init__(self,name):
#         self.__name=name
#         print("Created a school ",name)
    
#     def printer(self):
#         print("This is the school class function.")
#     def no_of_classes(self,classes):
#         self.__classes=classes
#         print("There are ",self.__classes," classes in ",self.__name)

# class College(Educational_institution):
#     __default="Beginners tutorials"
#     __subjects=[]
#     def get_default(self):
#         print(self.__default)

#     def __init__(self,name):
#         self.__name=name
#         print("Created a college ",name)

#     def no_of_classes(self,classes):
#         self.__classes=classes
#         print("There are ",self.__classes," classes in ",self.__name)

#     def courses_available(self,subject):
#         self.__subjects.append(subject)

#     def get_courses(self):
#         return self.__subjects
    
# class UG(College):
#     __subjects=[]
#     def __init__(self,name):
#         self.__name=name
#         print("Created a UG ",name)

#     def no_of_classes(self,classes):
#         self.__classes=classes
#         print("There are ",self.__classes," classes in ",self.__name)

#     def courses_added(self,subject):
#         self.__subjects.append(subject)

#     def get_courses(self):
#         print("this is the ug function.")
#         return self.__subjects
    

# class PG(College,School):
#     __subjects=[]
#     def __init__(self,name):
#         self.__name=name
#         print("Created a PG ",name)

#     def no_of_classes(self,classes):
#         self.__classes=classes
#         print("There are ",self.__classes," classes in ",self.__name)

#     def courses_added(self,subject):
#         self.__subjects.append(subject)

#     def get_courses(self):
#         print("this is the pg function.")
#         return self.__subjects
    
#     def get_collegeName(self):
#         print("The college name: ",self.__name)

#     def set_moto(**kwargs):
#         for i in kwargs:
#             print(i)
#     def __del__(self):
#         print("Object is deleted.")

# n_school=School("Narayana")
# c_college=College("CBIT")
# n_school.no_of_classes(20)
# c_college.no_of_classes(40)
# print(c_college.get_courses())

# ug= UG("Maruchusses")
# pg=PG("Moscow")
# pg.courses_added("Microbio")
# ug.courses_added("Biochem")
# print(pg.get_courses())
# print(ug.get_courses())

# def main():
#     list_of_colleges=[]
#     college_name="default"
#     while college_name!="":
#         college_name=input("Enter the college name: ")
#         list_of_colleges.append(PG(college_name))
#     for college in list_of_colleges:
#         college.get_collegeName()
    
# main()


# class shape():
#     def area():
#         pass
# class circle(shape):
#     def area(self,r):
#         return 3.15*r*r

# class square(shape):
#     def area(self,l):
#         return l*l

import random
import datetime
class customer_details:
    __current_ordersid=[]
    __completed_ordersid=[]
    def __init__(self):
        self.__customer_id = "cus"+str(random.randint(123456789,987654321))
    def set_current_orders(self,items):
        self.__current_ordersid.append(items)
    def get_customer_id(self):
        return self.__customer_id
    def update_order_status(self,order_id):
        if order_id in self.__current_ordersid:
            self.__completed_ordersid.append(order_id)
            self.__current_ordersid.remove(order_id)
        else:
            print("The order id is wrong")
    def get_customer_current_orders(self):
        return self.__current_ordersid
    def get_customer_completed_orderid(self):
        return self.__completed_ordersid
    
class order_details:
    def __init__(self, customer):
        self.__customer_id = customer.get_customer_id()
        self.assign_date_time()
        self.__order_id = "ref" + str(random.randint(123456789, 987654321))

    def get_order_id(self):
        return self.__order_id
    
    def assign_date_time(self):
        self.__date_time=datetime.datetime.now()
    def get_date_time(self):
        return self.__date_time
    def get_customer_id(self):
        return self.__customer_id
    
#create 2 customers
def create_new_customer():
    return customer_details()
# customer1=customer_details()
# customer2=customer_details()
def create_new_order(customer):
    temp =order_details(customer)    
    customer.set_current_orders(temp.get_order_id())
    return temp

def main():
    customers_list = []
    orders_list = []
    
    while True:
        print("\n1. Create new customer.")
        print("2. Create new order for customer.")
        print("3. Mark order as delivered.")
        print("4. View customer orders.")
        print("5. Exit")
        
        choice = int(input("Enter the operation you want to perform: "))
        
        if choice == 1:
            new_customer = create_new_customer()
            customers_list.append(new_customer)
            print(f"Customer created with ID: {new_customer.get_customer_id()}")
        
        elif choice == 2:
            customer_id = input("Enter the customer ID: ")
            customer = None
            for cust in customers_list:
                if cust.get_customer_id() == customer_id:
                    customer = cust
                    break
            if customer:
                new_order = create_new_order(customer)  
                orders_list.append(new_order)
                print(f"Order created with ID: {new_order.get_order_id()} for customer {customer_id}")
            else:
                print("Customer not found.")
        
        elif choice == 3:
            order_id = input("Enter the order ID to mark as delivered: ")
            order_found = False
            for order in orders_list:
                if order.get_order_id() == order_id:
                    for customer in customers_list:
                        if customer.get_customer_id() == order.get_customer_id():
                            customer.update_order_status(order_id)
                            print(f"Order {order_id} marked as delivered.")
                            order_found = True
                            break
                    break
            
            if not order_found:
                print("Order ID not found.")
        
        elif choice == 4:
            for customer in customers_list:
                print(f"Customer {customer.get_customer_id()} - Current Orders: {customer.get_customer_current_orders()} Completed Orders: {customer.get_customer_completed_orderid()}")
        
        elif choice == 5:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
#create 3 orders from customer 1
# order1=order_details(customer1.get_customer_id())
# order2=order_details(customer1.get_customer_id())
# order3=order_details(customer1.get_customer_id())

# #create 3 orders from customer2
# order4=order_details(customer2.get_customer_id())
# order5=order_details(customer2.get_customer_id())
# order6=order_details(customer2.get_customer_id())

# #assign the created orders 1 2 3  for the customer1
# customer1.set_current_orders(order1.get_order_id())
# customer1.set_current_orders(order2.get_order_id())
# customer1.set_current_orders(order3.get_order_id())

#update the order to completed
# customer1.update_order_status(order1.get_order_id())
# customer1.update_order_status(order2.get_order_id())
# customer1.update_order_status(order6.get_order_id())

# customer2.set_current_orders(order1.get_order_id())
# customer2.set_current_orders(order2.get_order_id())
# customer2.set_current_orders(order3.get_order_id())
#assign the created orders 4 5 6 for customer2
# customer2.set_current_orders(order4.get_order_id())
# customer2.set_current_orders(order5.get_order_id())
# customer2.set_current_orders(order6.get_order_id())

# #update the status to updated 
# customer2.update_order_status(order4.get_order_id())
# customer2.update_order_status(order5.get_order_id())
# customer2.update_order_status(order6.get_order_id())


# print("Customer 1:")
# print("current orders",customer1.get_customer_current_orders())
# print("completed orders",customer1.get_customer_completed_orderid())
# print("Customer 2:")
# print("current orders",customer2.get_customer_current_orders())
# print("completed orders",customer2.get_customer_completed_orderid())
