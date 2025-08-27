# Use the len() function on a string, list, tuple, and dictionary
a = "a b c"
string = len(a)
print(string)

b = [1,2,"c","hello"]
list = len(b)
print(list)

c = (1,"hello",2)
tuple = len(c)
print(tuple)

d = {"a":"hello","b":"hi"}
list = len(d)
print(list)


# Demonstrate the + operator working for Strings (concatenation), Lists (concatenation), Numbers (addition)
a = "aakriti"
b = "acharya"
string = a+b
print(string)

c = [1,3,"learn"]
d = ["python"]
list = c+d
print(list)

e = 20
f = 10
num = e+f
print(num)


# Write a function display(item)
def display(item):
    print(item)

obj1 = display(12)
obj2 = display("python")
obj3 = display([1,True])
obj4 = display({"a":"aakriti"})


# Create two classes: Dog and Cat
# Both should have a method sound() returning "Bark" and "Meow"
class Dog:
    def sound(bark):
        print("Dog is barking")
        return bark

class Cat:
    def sound(meow):
        print("Cat is meowing")
        return meow
    
# function that takes an animal object and calls sound()
def Animal(animal):
    animal.sound()

Animal(Dog())
Animal(Cat())


# Create a class Shape with a method area()
class Shape:
    def area(self):
        pass

class Square(Shape):
        
    def area(self,area1):
        area = area1 ** 2
        print(area)

class Circle(Shape):
    def area(self,radius):
        area = 22/7 * (radius ** 2)
        print(area)

# Inherit classes Square and Circle from it and override the area() method
sh1 = Square()
sh2 = Circle()
sh1.area(19)
sh2.area(28)

#Create a class Calculator with a method add()
#Make it accept Two arguments, Three arguments
class Calculator:
    def add(self,*args,**kwargs):
        return sum(args) + sum(kwargs.values())

ob1 = Calculator()  
print(ob1.add(1,2,3,4,10, k=9))

a = {}
print("a is:", type(a))

# Create two classes: Car and Bike , both with a method start() 
class Car:
    def start():
        print("Car started")

class Bike:
    def start():
        print("Bike started")

def start_vehicle(vehicle):
     vehicle.start()

start_vehicle(Car)
start_vehicle(Bike)

# create an abstract class Payment with a method process_payment()
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Implement classes: CreditCardPayment , PayPalPayment , and CryptoPayment overriding process_payment()
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Credit card processing payment")

class PayPalPayment(Payment):
    def process_payment(self):
        print("PayPal processing payment")

class CryptoPayment(Payment):
    def process_payment(self):
        print("Credit Card processing payment")

# Iterate over them in a list and call process_payment()
l1 = [CreditCardPayment() , PayPalPayment() , CryptoPayment()]
for i in l1:
    i.process_payment()
    


# Create classes: TextFileHandler , JSONFileHandler , CSVFileHandler
# Each should have methods: read() and write()
class TextFileHandler:
    def read(self):
        print("This reads Text File handler")

    def write(self):
        print("This writes Text File handler")

class JSONFileHandler:
    def read(self):
        print("This reads JSON File handler")

    def write(self):
        print("This writes JSON File handler")

class CSVFileHandler:
    def read(self):
        print("This reads CSV File handler")

    def write(self):
        print("This writes CSV File handler")
    
ob1 = TextFileHandler()
ob2 = JSONFileHandler()
ob3 = CSVFileHandler()

# same method name performs different tasks based on the object type.
ob1.read()
ob1.write()

ob2.read()
ob2.write()

ob3.read()
ob3.write()


 







    

    


