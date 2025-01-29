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

class Educational_institution:
    def __init__(self):
        print("Created a institution.")
    
    def Teachers(self):
        print("There are teachers.")
    
    def Students(self):
        print("There are students.")
    

    def no_of_classes(self):
        print("There are classrooms.")


class School(Educational_institution):

    def __init__(self,name):
        self.__name=name
        print("Created a school ",name)
    
    def no_of_classes(self,classes):
        self.__classes=classes
        print("There are ",self.__classes," classes in ",self.__name)

class College(Educational_institution):
    __subjects=[]
    def __init__(self,name):
        self.__name=name
        print("Created a college ",name)

    def no_of_classes(self,classes):
        self.__classes=classes
        print("There are ",self.__classes," classes in ",self.__name)

    def courses_available(self,subject):
        self.__subjects.append(subject)

    def get_courses(self):
        return self.__subjects
    
class UG(College):
    __subjects=[]
    def __init__(self,name):
        self.__name=name
        print("Created a UG ",name)

    def no_of_classes(self,classes):
        self.__classes=classes
        print("There are ",self.__classes," classes in ",self.__name)

    def courses_added(self,subject):
        self.__subjects.append(subject)

    def get_courses(self):
        return self.__subjects
    

class PG(College):
    __subjects=[]
    def __init__(self,name):
        self.__name=name
        print("Created a PG ",name)

    def no_of_classes(self,classes):
        self.__classes=classes
        print("There are ",self.__classes," classes in ",self.__name)

    def courses_added(self,subject):
        self.__subjects.append(subject)

    def get_courses(self):
        return self.__subjects


# n_school=School("Narayana")
# c_college=College("CBIT")
# n_school.no_of_classes(20)
# c_college.no_of_classes(40)
# print(c_college.get_courses())

ug= UG("Maruchusses")
pg=PG("Moscow")
pg.courses_added("Microbio")
ug.courses_added("Biochem")
print(pg.get_courses())
print(ug.get_courses())
