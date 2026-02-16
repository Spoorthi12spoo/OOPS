#Encapsulation

#private access
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance=initial_balance

    def withdraw(self, amount):
        if self.__balance>=amount:
            self.__balance-=amount
            print("Withdrawal successful. Remaining balance:",self.__balance)
        else:
            print("Insufficient funds. Balance remains:",self.__balance)

acc = BankAccount(1000)
acc.withdraw(200)
acc.withdraw(900)


class StudentResult:
    def __init__(self):
        self.__score=0
        
    def update_score(self, new_score):
        if new_score>self.__score:
            self.__score=new_score
            print(f"Score updated to {self.__score}")
        else:
            print(f"New score is lower. Score remains: {self.__score}")
                    
s = StudentResult()
s.update_score(70)


#protected access

class Product:
    def __init__(self, name, stock):
        self.name=name
        self._stock=stock

    def sell(self, quantity):
        if quantity<=self._stock:
            self._stock-=quantity
            return f"Sold {quantity} units of {self.name}"
        else:
           return f"Insufficient stock"
    def get_stock(self):
        return self._stock

p = Product("Laptop", 10)    
p.sell(3)   
p.sell(8)   
print(p.get_stock())



class SavingsAccount:
    def __init__(self, initial_balance):
        self._balance=initial_balance

    def add_interest(self):
        self._balance+=self._balance*5/100
        return self._balance

s1 = SavingsAccount(100)
print( round(s1.add_interest(), 2))


#public access

class Student:
    def __init__(self):
        self.present_days=0

s = Student()
s.present_days = 15
print(s.present_days)


class Course:
    def __init__(self):
        self.completed_modules=0

c = Course()
c.completed_modules = 5
print(c.completed_modules)