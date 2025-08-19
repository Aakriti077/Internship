#Print numbers from 1 to 10
for i in range(1,11):
    print(i)

#Print all even numbers
for i in range(2,51,2):
    print(i)

#Print the multiplication table of a number
num=5
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#sum of first 100 natural numbers
sum1=0
for i in range(0,101):
    sum1 += i
print(sum1)

#Print each character of a string
word = "Python"
for i in word:
    print(i)


#while loop
i = 1
while i<11:
    print(i)
    i += 1

#Keep asking the user for a number until they enter 0
while True:
    user = int(input("Enter your number: "))
    if user == 0:
        break
    else:
        print(user)    

#that prints numbers 10 down to 1
i=10
while i>=1:
    print(i)
    i -= 1

#keeps asking for a password until the correct one is entered.
while True:
    answer = input("Enter your password: ")
    if answer == "Python123":
        print("Answer is correct")
        break
    else:
        print("Try again")
        

# program that keeps rolling a dice (random 1–6) until it rolls a 6 
import random
while True:
    a = random.randint(1,6)
    if a==6:
        print(a)
        break
    else:
        print("Try again")


#Print numbers from 1 to 20, but skip multiples of 5
i = 1
while i<=19:
    i+=1
    if i % 5==0:
        continue
    print(i)

#Stop when they enter a negative number, then print the sum of all entered positive numbers
sum=0
while True:
  num1 = int(input("Enter numbers: "))
  if num1<0:
      print()
      break
  else:
    sum += num1
print(f"The sum of positive number is: {sum}") 

#checks if a number is prime
number1 = int(input("Enter the number: "))
for i in range(2,number1):  
    if number1 % i == 0:
      is_prime=False
      break
    else:
         is_prime=True   
if is_prime:
    print("num is prime")
else:
    print("num is not prime")


#first 10 Fibonacci numbers
num1 = 0
num2 = 1
for i in range(0,11):
    num1,num2 = num2, num1+num2
    print(num2)

#factorial num
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)


#Nested loops 
for i in range(5):
    for i in range(5):
        print("*" , end= "")
    print()

#Print a right-angled triangle
for i in range(5):
    for j in range(0,i+1):
        print("*", end= "")
    print()

#prints all pairs (i, j)
for i in range(1,4):
    for j in range(1,4):
        print((i,j))

#Print number pyramid
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#Simulate a bank account system
balance = 1000
while True:
    check = input("Enter your deposit amount:")
    if check == "exit":
        print()
        break
    elif check == "deposit1":
        deposit1 = input("Enter your deposit amount:")
        balance += deposit1
        print(f"Your new balance is {balance}")
    elif check == "withdraw":
        withdraw = input("Enter your deposit amount:")
        balance -= withdraw
        print(f"Your new balance is {balance}")
    else:
        print()














    


    



