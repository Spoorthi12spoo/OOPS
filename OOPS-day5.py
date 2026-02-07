#Hierarchical inheritance

class BankAccount:
    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.balance=0

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance: ",self.balance)

class SavingsAccount(BankAccount):
    def __init__(self,account_holder,interest_rate):
        super().__init__(account_holder)
        self.interest_rate=interest_rate

    def add_interest(self):
        self.balance+=self.balance*self.interest_rate/100
        super().display_balance()

class CurrentAccount(BankAccount):
    def __init__(self,account_holder,overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit=overdraft_limit

    def withdraw_with_overdraft(self,amount):

        if amount<=self.balance+self.overdraft_limit:
            self.balance-=amount
            print("withdrawn amount: ",amount)
            print("Balance: ",self.balance)

        else:
            print("Overdraft limit exceeded")

Savings=SavingsAccount("ABC",5)
Savings.add_interest()
Savings.deposit(1000)
Savings.withdraw(500)
Savings.display_balance()

current = CurrentAccount("XYZ",5000)
current.withdraw_with_overdraft(200)
current.display_balance()


# Hybrid Inheritance 

class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("\nPerson name:", self.name)


class Student(Person):
    def __init__(self, name, student_id):
        Person.__init__(self,name)     
        self.student_id = student_id

    def display_student(self):
        print("Student id:", self.student_id)


class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)   
        self.sport_name = sport_name

    def display_sports_player(self):
        print("Sports player:", self.sport_name)


class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        SportsPlayer.__init__(self,name,sport_name ) 
        Student.__init__(self,name,student_id)
        self.college_name = college_name

    def display_college_student(self):
        print("College name:", self.college_name)

stud1 = CollegeStudent("Alice", 1, "Cricket", "ABC")

stud1.display_person()
stud1.display_student()
stud1.display_sports_player()
stud1.display_college_student()

