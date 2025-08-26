# class Car:
#     __color = "blue"

#     def __start(self):
#         print("Starting car")


#     def get_color(self):
#         return self.__color
    
#     def set_color(self,new_color):
#         self.__color = new_color
#         # return new_color

# c1 = Car()

# print(c1.get_color())
# # print(c1.get_color())
# c1.set_color("red")

# print(c1.get_color())
# # c1.__start()



class Car:
    color = "red"
    __color = "green"
    __color = "blue"

    def __start(self):
        print("Starting car")


    def get_color(self):
        return self.__color
    
    def set_color(self,new_color):
        self.__color = new_color
        # return new_color

c1 = Car()
print(dir(c1))

#Name mangling
print(c1._Car__color)

#method lai attribute jasari access property le  

#decorator is function has @, certain function add
class Car:
    __color = "blue"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,new_color):
        self.__color = new_color

c1 = Car()
print(c1.color)
c1.color = "pink"
print(c1.color)