#Create a class Car with attributes brand and color 
#Create two objects
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

car1 = Car("Byd","Mint")
car2 = Car("Audi","Black")

print(car1.brand, car1.color)
print(car2.brand, car2.color)


#Create a class Student with attribute name
class Student:
    def __init__(self,name):
        self.name = name

#Add a method greet() to print: "Hello, I am <name>"
    def greet(self):
        print(f"Hello I am {self.name}")

student1 = Student("aakriti")
student2 = Student("ram")
student3 = Student("niroj")
print(student1.name)
student1.greet()
student2.greet()
student3.greet()



#Create a class Dog with an attribute name
class Dog:
    def __init__(self,name):
        self.name=name

#Add a method bark() that prints: "<name> is barking!"
    def bark(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Leo")
dog2 = Dog("Goldy")    
dog1.bark()
dog2.bark()  


class BankAccount:
    def __init__(self,account_num, balance=0):
        self.account_num = account_num
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount

        print(f"The deposited amount is: {amount}")

    def withdraw(self,amount):
        self.balance -= amount

        print(f"The withdrawn amount is: {amount}")

    def show_balance(self):

        print(f"The balance amount is: {self.balance}")

deposit1 = BankAccount("1234")  #account create
deposit1.deposit(1000)
deposit1.withdraw(100)
deposit1.show_balance()


#Create a class Book
class Book:
    category = "Fiction"   #Class attribute

    def __init__(self,title,author):    #Instance attribute
        self.title = title
        self.author = author

    def display(self):   #Method
        print(f"Title: {self.title}")
        print(f"Category: {Book.category}")
        print(f"Author: {self.author}")

book1 = Book("Verity","Coolen Hoover")    #Create two books
book2 = Book("Harry Potter","Aakriti")

print("Book details: ")       
book1.display()           #display their details
book2.display()


#Create a class Rectangle
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        area1 = self.length*self.width
        print(f"The area is: {area1}")

    def perimeter(self):
        perimeter1 = 2*(self.length+self.width)
        print(f"The perimeter is: {perimeter1}")

rectangle1 = Rectangle(8,4)
rectangle2= Rectangle(6,2)

rectangle1.area()
rectangle1.perimeter()
rectangle2.area()
rectangle2.perimeter()


#Create a class ShoppingCart 
class ShoppingCart:
    def __init__(self,shopping_cart = []):
        self.shopping_cart = shopping_cart   

    def add_item(self,item):
        self.shopping_cart.append(item)
        print(f"Added item is: {item}")

    def remove_item(self,item):
        self.shopping_cart.remove(item)
        print(f"Removed item is: {item}")

    def show_cart(self):
        print(f"Total item in list is: {self.shopping_cart}")

cart1=ShoppingCart()
cart1.add_item("Apple", "ok")
cart1.add_item("b")
cart1.add_item("a")
cart1.remove_item("b")
cart1.show_cart()


class Counter:
    def __init__(self,count=0):
        self.count = count 

    def increment(self):
        self.count += 1
        print(self.count)

    def reset(self):
        self.count = 0
        print(self.count)
    
counter1 = Counter()
counter1.increment()
counter1.reset()


class TemperatureConverter:


    def c_to_f(self, celcius):
        c = (celcius * 9/5)+32 
        print(f"This is celcius: {c}")

    def f_to_c(self, fahrenight):
        f = (fahrenight - 32) * 5/9
        print(f"This is fahrenheit: {f}")  

temp1 = TemperatureConverter()
temp1.c_to_f(12)
temp1.f_to_c(90)

class Movie:
    def __init__(self,title,genre,rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def is_recommend(self):
        if self.rating >= 8:
            return True
        else:
            return False

movie1 = Movie("Avatar","Fiction",9)
movie2 = Movie("Hello","Action",4)
movie3 = Movie("World","Real world",7)
print(movie1.is_recommend())
print(movie2.is_recommend())
print(movie3.is_recommend())

        




        