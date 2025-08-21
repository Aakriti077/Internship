import random

num1 = random.randint(1,100)
print(f"Random number is: {num1}")

num = [1,2,3,4,5,6]
random.shuffle(num)
print(f"Suffled number is: {num}")

element1 = ["aakriti",1,2,"hello","saugat","python"]
choice=random.choice(element1)
print(f"The random element is: {choice}")
