#Create a Vehicle class with attributes brand and speed and a method move() 
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print("The car is moving")

#Inherit it in a Car class, add an attribute num_doors , and method honk() 
class Car(Vehicle):
    def __init__(self, num_doors):
        self.num_doors = num_doors

    def honk(self):
        print("The car is honking")

#Instantiate Car and call both parent and child methods
car1 = Car(4)
print(f"The number of doors is: {car1.num_doors}")
car1.brand = "Byd"
car1.speed = 200
print(f"The car brand is: {car1.brand}")
print(f"The car speed is: {car1.speed}")
car1.move()
car1.honk()


#Modify Parent Property
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print("The car is moving")

#Inherit it in a Car class, add an attribute num_doors , and method honk() 
class Car(Vehicle):
    def __init__(self, num_doors):
        self.num_doors = num_doors

    def honk(self):
        print("The car is honking")

    def change_brand(self,new_brand):
        self.brand = new_brand

#Instantiate Car and call both parent and child methods
car1 = Car(4)
print(f"The number of doors is: {car1.num_doors}")

car1.brand = "Byd"
car1.speed = 200

print(f"The car brand is: {car1.brand}")
print(f"The car speed is: {car1.speed}")

car1.change_brand("kia")
print(f"The new car brand is: {car1.brand}")

car1.move()
car1.honk()


#Add an __init__() method in Vehicle with brand and speed
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        

#Add Car with its own __init__() using super() to call Vehicle 's constructor
class Car(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)

#Extend it to ElectricCar with battery capacity
class ElectricCar(Car):
    def __init__(self,brand,speed,battery):
        super().__init__(brand,speed)
        self.battery = battery

car1 = ElectricCar("byd","200mph","24hr")

print(f"The brand is: {car1.brand}")
print(f"The speed is: {car1.speed}")
print(f"The battery capacity is: {car1.battery}")


#Add an __init__() method in Vehicle with brand and speed
class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print("The car is moving at 300km/h")

#Add Car with its own __init__() using super() to call Vehicle 's constructor
class Car(Vehicle):
    def __init__(self,brand,speed):
        super().__init__(brand,speed)
        

    def move(self):
        print("The car is moving at 500km/h")
        super().move()

car1 = Car("byd","200mph")

car1.move()

print(f"The brand is: {car1.brand}")
print(f"The speed is: {car1.speed}")


#Multiple inheritance
class Car:
    def show_location(self):
        print("This shows location of Car")

    def move(self):
        print("The car is moving at 500km/h")
        
class GPS:
    def move(self):
        print("The car is moving at 200km/h")

    def show_location(self):
        print("This shows location of GPS")

# class SmartCar(Car,GPS):
#     pass

class SmartCar(GPS,Car):
    pass

car1 = SmartCar()
car1.move()
car1.show_location()


#Vehicle → Car → SportsCar
class Vehicle:
    def part(self):
        print("This vehicle has engine")

class Car(Vehicle):
    def color(self):
        print("The car is black")

#Instantiate SportsCar and access methods from all levels
class SportsCar(Car):
    def speed(self):
        print("This is very fast")
    pass

car1 = SportsCar()
car1.speed()
car1.color()
car1.speed()


#Demonstrate each child's unique behavior
class Vehicle:
    def __init__(self,engine):
        self.engine = engine
        print(f"The engine is: {self.engine}")

class Bike(Vehicle):
    def __init__(self, speed):
        self.speed = speed
        print(f"The speed is {self.speed} of class bike")

class Truck(Vehicle):
    def __init__(self, color):
        self.color = color
        print(f"The color is {self.color} of class truck")


obj1 = Bike("120mph")
obj2 = Truck("Blue")

obj1.speed
obj2.color


#Create multiple animals
#Feed them using the ZooKeeper class
#WildLion inherits from Lion ) and override behavior

class Animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} eats food.")

class ZooKeeper:
    def food(self):
        print(f"They feed food to {self.name}")

class Lion(Animal,ZooKeeper):
    def roar(self):
        print(f"{self.name} roars loudly")

class Elephant(Animal,ZooKeeper):
    def spray_water(self):
        print(f"{self.name} sprays water")

class WildLion(Lion):
    def roar(self):
        print(f"{self.name} roars even loudly")

l1 = Lion("Leo",12,"Wild")
l1.food()
l1.roar()

wl1 = WildLion("Simba",6,"Wild")
wl1.roar()