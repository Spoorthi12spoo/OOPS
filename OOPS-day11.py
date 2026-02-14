#Hierarchical inheritance

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name,age)
        self.grade=grade

    def get_details(self):
        return f"{self.name} is {self.age} years old and studies in {self.grade} grade."

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name,age)
        self.subject=subject

    def get_details(self):
        return f"{self.name} is {self.age} years old and teaches {self.subject}."

s1 = Student("Asha", 15, "10th")
print( s1.get_details())

class Person:
    def __init__(self, name, emp_id):
        self.name=name
        self.emp_id=emp_id

class Manager(Person):
    def __init__(self, name, emp_id, department):
        super().__init__(name,emp_id)
        self.department=department

    def get_profile_data(self):
        return f"{self.name} (ID: {self.emp_id}) is a manager of {self.department} department."
        

class Engineer(Person):
    def __init__(self, name, emp_id, specialization):
        super().__init__(name,emp_id)
        self.specialization=specialization

    def get_profile_data(self):
         return f"{self.name} (ID: {self.emp_id}) is a {self.specialization.lower()} engineer."

m1 = Manager("Kavita", 101, "HR")
print( m1.get_profile_data())

class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author

class Novel(Book):
    def __init__(self, title, author, genre):
        super().__init__(title,author)
        self.genre=genre

    def details(self):
        return f"'{self.title}' by {self.author} is a {self.genre} novel."

class Magazine(Book):
    def __init__(self, title, author, issue):
        super().__init__(title,author)
        self.issue=issue

    def details(self):
        return f"'{self.title}' by {self.author}, Issue: {self.issue}."

n1 = Novel("The Alchemist", "Paulo Coelho", "Fiction")
print( n1.details())


#Hybrid inheritance

class Device:
    def __init__(self, brand):
        self.brand=brand

class VoiceControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    def voice_activate(self):
        return "voice"

class AppControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    def app_activate(self):
        return "app"
class SmartSpeaker(VoiceControl, AppControl):
    def __init__(self,brand):
        super().__init__(brand)
    def control_methods(self):
        return f"{self.brand} can be controlled via {self.voice_activate()} and {self.app_activate()}."

s1 = SmartSpeaker("Echo")
print( s1.control_methods())


class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

class Faculty(Person):
    def __init__(self, subject, **kwargs):
        super().__init__(**kwargs)
        self.subject = subject

    def teach(self):
        return self.subject

class Staff(Person):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

    def work(self):
        return self.department

class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        super().__init__(name=name, subject=subject, department=department)

    def profile_data(self):
        return f"{self.name} teaches {self.teach()} and works in {self.work()} department."