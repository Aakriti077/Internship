class House:   #class
    def __init__(self,color):    #constructor  , attribute
        print("Inside class",self)    #self obj ho tya affai janxa
        self.color = color

    def ring_the_bell(self):   
        print("Bell Ranggg",self)

    def change_the_color(self,new_color):
        self.color = new_color

        

house1 = House("Red")    
house2 = House("Yellow")

print("House1 initial color: ",house1.color)
print("House1 initial color: ",house2.color)

#after change
house1.change_the_color("Pink")
house2.change_the_color("White")

print("House1 new color: ",house1.color)
print("House1 new color: ",house2.color)




