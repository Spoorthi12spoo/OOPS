#Polymorphism(Method overriding)

class Payment:
    def pay(self):
        print("Payment")

class GooglePay(Payment):
    def pay(self):
        print("GooglePay Payment")

class PhonePe(Payment):
    def pay(self):
        print("PhonePay payment")

class CreditCard(Payment):
    def pay(self):
        print("CreditCard payment")


payment1=Payment()
payment1.pay()

Gpay=GooglePay()
Gpay.pay()

phonepe1=PhonePe()
phonepe1.pay()

creditcard1=CreditCard()
creditcard1.pay()

#Abstraction

from abc import ABC,abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine is starting")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine is started")
    
class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine is starting")

car1=Car()
car1.start_engine()


bike1=Bike()
bike1.start_engine()


bus1=Bus()
bus1.start_engine()