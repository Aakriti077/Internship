from abc import ABC, abstractmethod

# Create an abstract class Shape
# Abstract methods: area() , perimeter()
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#Create classes Rectangle and Circle inheriting from Shape and implement those methods
class Rectangle(Shape):

    def area(self,length,width):
        area = length * width
        print(f"Area is: {area}")

    def perimeter(self,length,width):
        perimeter = 2 * (length + width)
        print(f"Perimeter is: {perimeter}")

class Circle(Shape):
    def area(self,radius):
        area = 22/7 * (radius**2)
        print(f"Area is: {area}")

    def perimeter(self,radius):
        perimeter = 2 * (22/7 * radius)
        print(f"Perimeter is: {perimeter}")

r1 = Rectangle()
c1 = Circle()

r1.area(2,4)
r1.perimeter(2,5)

c1.area(4)
c1.perimeter(2)


#Create an abstract class Vehicle with abstract methods start() , stop() , and fuel_type() 
class Vehicle:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# Create Car and Bike classes
class Car(Vehicle):
     def start(self):
        print("Car has started")

     def stop(self):
        print("Car has stoppped")

     def fuel_type(self):
        print("Car has full fuel")

class Bike(Vehicle):
    def start(self):
        print("Bike has started")

    def stop(self):
        print("Bike has stoppped")

    def fuel_type(self):
        print("Bike has half fuel")

v1 = Car() 
v2 = Bike()

v1.start()
v1.stop()
v1.fuel_type()

v2.start()
v2.stop()
v2.fuel_type()


#Abstract class PaymentGateway with methods authenticate() ,process_payment(amount) , refund(amount)
class PaymentGateway(ABC):
    
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def process_payment(self,amount):
        pass

    @abstractmethod
    def refund(self,amount):
        pass

# Implement classes:
# CreditCardPayment
# PayPalPayment
# CryptoPayment
class CreditCard(PaymentGateway):
    def authenticate(self):
        print("Authenticating credit card details")

    def process_payment(self,amount):
        print(f"Processing Payment {amount}")

    def refund(self,amount):
        print(f"Giving Refund {amount}")

class PayPalPayment(PaymentGateway):
    def authenticate(self):
        print("Authenticating PayPal details")

    def process_payment(self,amount):
        print(f"Processing Payment {amount}")

    def refund(self,amount):
        print(f"Giving Refund {amount}")

class CryptoPayment(PaymentGateway):
    def authenticate(self):
        print("Authenticating Crypto payment details")

    def process_payment(self,amount):
        print(f"Processing Payment {amount}")

    def refund(self,amount):
        print(f"Giving Refund {amount}")

p1 = CreditCard()
p2 = PayPalPayment()
p3 = CryptoPayment()

p1.authenticate()
p1.process_payment(200)
p1.refund(100)

p1.authenticate()
p1.process_payment(300)
p1.refund(100)

p1.authenticate()
p1.process_payment(500)
p1.refund(200)



class LibraryItem(ABC):
    pass

    def checkout(self):
        pass

    def return_item(self):
        pass

class Book:
    pass

class Magazine:
    pass 

class DVD:
    pass
