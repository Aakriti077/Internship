# #Parent class
# class Parent:
#     surname = "Acharya"

#     def family_surname(self):
#         print(f"This is our surname: {self.surname}")
    
#     def breakfast(self):
#         print("This is bread")

# #Child class
# class Child(Parent):
#     def breakfast(self):
#         print("This is cookie")
        
    
# c1 = Child()
# c2 = Child()

# print(c1.surname)
# print(c1.surname)
# c1.breakfast()
# c2.breakfast()
# c1.family_surname()
# c2.family_surname()


# #Multilevel 
# class GrandParent:
#     def eye_color(self):
#         print("Eye is blue")

# class Parent(GrandParent):
#     def eye_color(self):
#         print("Eye is red")

#     def hair_color(self):
#         print("Hair is black")

# class Child(Parent):
#     def eye_color(self):
#         print("My eye color is brown")

#     def hair_color(self):
#         print("My hair color is red")

#     def height(self):
#         print("My height is 5ft")

# c1 = Child()
# c1.eye_color()
# c1.hair_color()
# c1.height()


# #Multiple
# class Father():
#     def drivig(self):
#         print("Good at driving")

#     def cooking(self):
#         print("Veryyy good at cooking")
    

# class Mother():
#     def cooking(self):
#         print("Good at cooking")

#     def driving(self):
#         print("Good very good")

# class Child(Mother,Father):
#     pass

# c1 = Child()
# c1.drivig()
# c1.cooking()


# #Hierarchical
# class Parent():
#     surname = "Acharya"
#     def land(self):
#         print("This is land")

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# child1 = Child1()
# print(child1.surname)
# child1.land()
# child2 = Child2()
# print(child1.surname)
# child2.land()


# class Parent():
#     def lunch(self):
#         print("we ate samosa")

# class Child(Parent):
#     def lunch(self):
#         print("we ate momo")
#         super().lunch()

# c1 = Child()
# c1.lunch()

