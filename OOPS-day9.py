#Dunder methods

#__str__() and __repr__()
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"Book(Book title:{self.title}, author name: {self.author}, price: {self.price})"

    def __repr__(self):
         return f"Book title:{self.title!r}, author name: {self.author!r}, price: {self.price}"


book1=Book("The art of being alone","XYZ",1000)
print(book1)
print(repr(book1))

#__eq__()

class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    
    def __eq__(self,other):
        return(
            self.brand==other.brand and
            self.model==other.model and
            self.price==other.model
        )

mobile1=Mobile("Apple","iphone15",40000)
mobile2=Mobile("Apple","iphone16",50000)
mobile3=Mobile("Apple","iphone17",100000)
print(mobile1==mobile2==mobile3)


#__new__ and __init__

class User:
    def __init__(self,name):
        self.name=name
        print("Object is initialized")
    
    def __new__(cls,name):
        print("Object is created")
        return super().__new__(cls)

user1=User("ABC")

#__enter__ and __exit__

class DatabaseConnection:
    def __enter__(self):
        print("Database Connected")
    def __exit__(self,exc_type,exc_val,exc_tab):
        print("Database Closed")
with DatabaseConnection():
    print("Performing Query..")