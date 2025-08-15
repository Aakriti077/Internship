#Store your age and print 
age = 21
print(age)

#Store price of item in float and print
price = 200.25
print(price)

#Add, subtract, multiply, and divide two integers
a = 5
b = 3
print(f"The sum is: {a+b}")

print(f"The difference is: {a-b}")

print(f"The multiply is: {a*b}")

print(f"The division is: {a/b}")


#Divide two integers and show:
c = 10
d = 3
print(f"The normal division is: {c/d}")  #Normal division

print(f"The floor division is: {c//d}")  #Floor division

print(f"The modulus division is: {c%d}")   #Modulus

#Multiply a float by an integer and print the result
m = 50.5
n = 4
print(f"The multiplication is: {m*n}")

#Use type() to check the data type of each result
print(type(age))
print(type(price))
print(type(a+b))
print(type(a-b))
print(type(a*b))
print(type(a/b))
print(type(c/d))
print(type(c//d))
print(type(c%d))
print(type(m+n))

#Convert temp from celcius to fahrenheit
celcius = float(input("Enter the celcius: "))
fahrenheit = (celcius*9/5) +32
print(f"The temprature is {fahrenheit}°C")

#Calculate circle area
radius = float(input("Enter the radius for area: "))
area = 22/7*(radius**2)
print(f"The area of circle is: {area}")

#Calculate circle circumference
radius1 = float(input("Enter the radius for circumference: "))
circumference = 2*22/7*radius1
print(f"The circumference of circle is: {circumference}")

#use abs() to find difference
a = -5
b = 10
print(f"The answer is: {abs(a-b)}") #abs()= - sign hatauxa

#Use round()
num = 3.14159

decimal = round(num,2)  #round function  use garni first ma value second ma up tp how many decimal round garni
print(f"The rounded decimal up to 2 decimal places is: {decimal}")

no_decimal = round(num)
print(f"The rounded decimal with no decimal places is: {no_decimal}")

#floor division
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print(f"The result is : {num1//num2}")  

#Convert a float to an integer
float1 = 40.0
int1 = int(float1)
print(f"The integer is: {int1}")

#convery string to float and add 10
string1 = "25.5"
float1 = float(string1)+10
print(f"The converted number is: {float1}")

print(type(float1))


#use max() and min to find 3 large and small numbers
input1 = int(input("Enter the first num: "))
input2 = int(input("Enter second num: "))
input3 = int(input("Enter third num: "))

max_num = max(input1, input2, input3)
min_num = min(input1, input2, input3)

print(f"The max number is: {max_num}")
print(f"The min number is: {min_num}")

#use sum()
list1=[1,5,7,8,5]
sum1 = sum(list1)
print(f"The sum is: {sum1}")

#generate random integer
import random
random1 = int(random.randint(1,100))
print(f"The random number is: {random1}")

#even or odd
text1 = int(input("Enter your number: "))
if text1 % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

#find compound interest
principal = int(input("Enter the principal: "))
rate = int(input("Enter your rate: "))
interest = int(input("Enter your interest: "))
time = int(input("Enter your time: "))
ci = principal*(1+rate/interest)**(interest*time)
print(f"The compound interest is: {ci}")

#convert
total_second = int(input("Enter your time in seconds: "))
hours = total_second // 3600
minute = (total_second % 3600) //60 
seconds = total_second % 6
print(f"The total second is: {hours}:{minute}:{seconds}")

#calculate distance
value1 = int(input("Enter value of x1: "))
value2 = int(input("Enter value of x2: "))
value3 = int(input("Enter value of y1: "))
value4 = int(input("Enter value of y2: "))
distance1 = ((value2-value1)**2+(value4-value3)**2)**0.5
print(f"The distance is: {distance1}")
