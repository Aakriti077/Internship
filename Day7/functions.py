#function greet(name) that takes a person’s name and prints "Hello, <name>!"
def greet(name):
    print(f"Hello, {name}")

greet("Aakriti")

#function add_numbers(a, b) that returns the sum of two numbers
def add_numbers(a,b):
     print(a+b)

a = add_numbers(1,2)

#function is_even(num) that returns True if the number is even, otherwise False
def is_even(num):
    return num % 2 == 0
num = int(input("Enter number: "))
if is_even(num):
        print("True")
else:
        print("False")

#a function factorial(n) that returns the factorial of a given number using aloop

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result    
           
num = int(input("Enter a number: "))
print(f"Factorial is {factorial(num)}")
      

#function convert_to_celsius(fahrenheit) that converts Fahrenheit to Celsius
def convert_to_celcius(fahrenheit):
    celcius = (fahrenheit-32)*5 / 9
    return celcius

print(convert_to_celcius(55))

#a function calculate_area(length, width=5) that calculates the area of a rectangle
def calculate_area(length, width=10):
    area = length * width
    return area

print(f"The area is: {calculate_area(10)}")

#a function power(base, exponent=2) that returns base raised to the power of exponent
def power(base, exponent=2):
    square = base ** exponent
    return square

print(f"The power raised is: {power(2)}")

#function count_vowels(word) that returns the number of vowels in a string.
def count_vowels(word):
    vowels = "aeiou"
    count = 0 
    for i in word:
        if i in vowels:
            count += 1
    return count

print(f"The vowels is: {count_vowels("python")}")
    
#a function reverse_string(s) that returns the reversed version of the string.
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

#a function max_of_three(a, b, c) that returns the largest of three numbers
def max_of_three(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(max_of_three(9,8,3))


#a function sum_all(*numbers) that returns the sum of all numbers passed
def  sum_all(*numbers):
    a = sum(numbers)
    # total = 0
    # for num in numbers:
    #     total += num
    # return total
print(sum_all(1,2,3))

#a function multiply_all(*numbers) that multiplies all numbers passed
def multiply_all(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
print(multiply_all(5,1,5))

#a function print_details(**info) that accepts name, age, and city as keyword arguments and prints them
def print_details(**info):
    if "name" in info:
        print(f"Name: {info['name']}")
    if "age" in info:
        print(f"Age: {info['age']}")
    if "city" in info:
        print(f"City: {info['city']}")

print_details(age= 12,city= "Kathmandu")

#a function describe_pet(animal, **details) that prints details about the pet
def describe_pet(animal, **details):
    print(f"Animal: {animal}")
    for key,value in details.items():
        print(f"{key.capitalize()}: {value}")
describe_pet("cat",name="Leo",age=1,color="white")

#a function average(*numbers) that returns the average of given numbers
def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
print(average(10,25,30))
    

