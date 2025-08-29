# a lambda function to calculate the cube of a given number
cube = lambda num:num**3
print(cube(3))

# lambda function that checks if a given string is a palindrome
word = lambda word1: word1 == word1[::-1]
print(word("Wow"))


# Map Function
# to convert a list of temperatures in Celsius to Fahrenheit
list1 = [12,35,70]

calc = lambda temp: (temp * (9/5) + 32)

res = map(calc,list1)
print(list(res))

# to return the length of each string
list2 = ["Aakriti", "Hello", "Python"]

names = lambda name:len(name)

res = map(names,list2)
print(list(res))


# Reduce Function
# to find the product of all numbers in a given list
from functools import reduce

list3 = [1,2,3,4]

mul = lambda num1,num2 : num1*num2

res = reduce(mul,list3)
print(res)


# to find the longest word from a list of words

from functools import reduce

list4 = ["peanuts","chocolate","cup"]

long = lambda a,b:a if len(a)>len(b) else b

res = reduce(long,list4)
print(res)


# to extract all even numbers from a list
list5 = [1,2,3,4,5,6]

even = lambda num1: True if num1 % 2 == 0 else False

res = filter(even,list5)
print(list(res))


# lambda to return only the words that start with the letter "A"

list6 = ["Aakriti","Food","Python","Hello","Apple"]

words = lambda name: True if name[0] == "A" else False

res = filter(words,list6)
print(list(res))


# use a combination of map() and filter() to square only the even numbers
list1 = [1,2,3,4,5,6]

num1 = lambda num: True if num % 2 == 0  else False
num2 = lambda num:num**2

res =map(num2,list(filter(num1,list1)))
print(list(res))



# use filter() to find all positive numbers, then use reduce() to calculate their sum

from functools import reduce

list2 = [1,5,7,0,-7,-2,-4]

num = lambda num1: True if num1 > 0 else False
num2 = lambda num1,num2 : num1+num2

res = reduce(num2,list(filter(num,list2)))
print(res)


# Create a program that takes a list of words
wlist = ["hello","world","how","are","learn","python",]

# filters out the words with length less than 4
word1 = lambda word: True if len(word) > 4 else False

# convert the remaining words to uppercase
word2 = lambda word: word.upper()

res = map(word2, list(filter(word1,wlist)))
print(list(res))


# together to calculate the sum of cubes of all odd numbers 
from functools import reduce

list1 = [1,2,3,4,5]

odd1 = lambda num: True if num % 2 != 0 else False

cube = lambda num: num ** 3

sum1 = lambda num,num2: (num+num2)


res = reduce(sum1,list(map(cube,list(filter(odd1,list1)))))
print(res)


# use map() to split them into words, then use reduce() to count the total number of words
from functools import reduce

sents = ["Hello my name is aakriti"]

split1 = lambda word: len(word.split())

count1 = lambda a,b: a+b

res = reduce(count1,list(map(split1,sents)))

print(res)


