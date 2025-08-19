#wap to check if num is is positive, negative, or zero
input1 = 0
if 0<input1:
    print("Number is positive")
elif 0>input1:
    print("Number is negative")
else:
    print("Number is zero")

#take age input and print accordingly
age = int(input("Enter your age: "))
if age<=13:
    print("Child")
elif age>13 & age<=19:
    print("Teenager")
else:
    print("Adult")

#checks whether a given number is even or odd
number1 = int(input("Enter the number: "))
if number1 %2 == 0:
    print("Number is even")
else:
    print("Number is odd")


#the password matches or not
password = input("Enter your password: ")
if password == "Python123":
    print("Access Granted")
else:
    print("Access Denied")


#If the temperature is above 30 print "It's hot"print else "It's normal" .
temp = float(input("Enter the tempreture: "))
if temp>30:
    print("Its hot")
else:
    print("Its normal")

#using and and nad noy
is_raining=input("is it rainig say yes or no: ")
has_umbrella=input("do you have umbrella yes or no: ")

if is_raining=="yes":
    is_raining=True
if has_umbrella=="yes":
    has_umbrella=True
if is_raining=="no":
    is_raining=False
if has_umbrella=="no":
    has_umbrella=False

if is_raining and has_umbrella:
    print("You can go outside")
elif is_raining and  has_umbrella==False:
    print("Stay Inside")


#Grading system
grade= int(input("Enter your grade: "))
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F")

#Traffic system
traffic = input("Enter the Traffic Light Color: ")
if traffic == "Red":
    print("Stop")
elif traffic == "Yellow":
    print("Get Ready")
elif traffic == "Green":
    print("Go")
else:
    print("Invalid Color")


#division
nums = int(input("Enter the number: "))
if nums % 3==0 and nums % 5==0:
    print("FizzBuzz")
elif nums % 3==0:
    print("Fizz")
elif nums % 5==0:
    print("Buzz")
else:
    print(nums)


#ATM Simulation
balance = 10000
amount = int(input("Enter your amount to withdraw: "))
if balance>=amount:
    print("Transaction Sucessfull")
else:
    print("Insufficient balance")

#Login system
username = "aakriti"
password = "123456"

username1 = input("Enter your username: ")
password1 = input("Enter your password: ")
if username==username1 and password==password1:
    print("Login Successful")
elif username!=username1:
    print("Invalid username")
elif password!=password1:
    print("Invalid password")

#check if person is eligible to vote
age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote")
if age >=16:
    print("You are eligible to Drive")
if age >=21:
    print("You are eligible to Drink Alcohol")
else:
    print("You are not eligible for anything")
    

#rock paper scissor
import random
choices = ["rock","paper","scissor"]
computer = random.choice(choices)
users = input("Choose rock, paper or scissors: ")
print(f"Computer chooses {computer}")
if users=="rock" and computer=="paper":
    print("User wins")
elif users=="rock" and computer=="rock":
    print("Draw")
elif users=="rock" and computer=="scissors":
    print("User wins")
elif users=="paper" and computer=="rock":
    print("Equal")
elif users=="paper" and computer=="paper":
    print("Draw")
elif users=="paper" and computer=="scissors":
    print("Computer wins")
elif users=="scissors" and computer=="rock":
    print("Computer wins")
elif users=="scissors" and computer=="paper":
    print("User wins")
elif users=="scissors" and computer=="scissors":
    print("Draw")
else:
    print("Invalid choice")


#quiz game
question1 = input("What is the capital of France? ")
question2 = input("Which is the highest mounatin of the world? ")
question3 = input("What is the largest planet in solar system? ")
point = 0
if question1=="Paris":
    point +=1
elif question2=="Mt.Everest":
    point +=1
elif question3=="Jupiter":
    point +=1
else:
    print(f"Your total score is:{point}")

