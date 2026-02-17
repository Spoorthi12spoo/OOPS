#Interfaces

from abc import ABC, abstractmethod
class ControllableDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(ControllableDevice):
    def turn_on(self):
        return f"Smart Light is now ON"

class SmartFan(ControllableDevice):
    def turn_on(self):
        return f"Smart Fan is now ON"

light = SmartLight()
print( light.turn_on())



from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class StripePayment(PaymentGateway):
    def pay(self,amount):
        return f"Paid ₹{amount} using Stripe"

class PaytmPayment(PaymentGateway):
    def pay(self,amount):
        return f"Paid ₹{amount} using Paytm"

stripe = StripePayment()
print( stripe.pay(100))



from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print_content(self):
        pass

class PDFDocument(Printable):
    def print_content(self):
        return f"Printing PDF Document"

class Image(Printable):
    def print_content(self):
        return f"Printing Image File"

pdf = PDFDocument()
print( pdf.print_content())



from abc import ABC, abstractmethod
class Movable(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Movable):
    def move(self):
        return f"Car is driving"

class Bike(Movable):
    def move(self):
        return f"Bike is riding"

c = Car()
print( c.move())