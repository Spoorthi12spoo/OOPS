# from abc import ABC,abstractmethod;
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#     def sleep(self):
#         print("Animal is sleeping..")

# class Dog(Animal):
#     def sound(self):
#         print("Bark..")
   

# class Cat(Animal):
#     def sound(self):
#         print("Meow..")
  
# class Cow(Animal):
#    def sound(self):
#          print("Moo..")

# dog1=Dog()
# dog1.sleep()
# dog1.sound()

# cat1=Cat()
# cat1.sleep()
# cat1.sound()

# cow1=Cow()
# cow1.sleep()
# cow1.sound()

# Animal.sleep()


#class,static,instance methods

# class Student:
#     college_name="ABC College"
#     def __init__(self,name,roll_no):
#         self.name=name
#         self.roll_no=roll_no

#     @classmethod
#     def change_college(cls,new_name):
#         cls.college_name=new_name

#     @staticmethod
#     def is_pass(marks):
#         if marks>=35:
#             print("pass")
#         else:
#             print("fail")

#     def display(self):
#         print(f"Student name:{self.name} Roll no: {self.roll_no} College Name: {self.college_name}")

# print(Student.college_name) 

# Stud1=Student("Alice",1)
# Student.change_college("XYZ college")
# Student.is_pass(30)
# Stud1.display()         

# Stud2=Student("Bob",2)
# Student.is_pass(80)
# Stud2.display()


#Decorators


def admin_only(dashboard):
    def wrapper(username):
        if username=="admin":
            dashboard(username)
        else:
            print("Access denied")
    return wrapper
        
@admin_only
def dashboard(username):
    print("Welcome to dashboard")

dashboard("admin1")