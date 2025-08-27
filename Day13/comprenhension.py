# List comprehension

# Generate a list of squares for numbers from 1 to 20
print([num**2 for num in range(1,21)])


# Extract all even numbers from a given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i for i in numbers if i %2 == 0])


# Create a list of their first letters
words = ["apple", "banana", "cherry", "date"]
print([i[0] for i in words])


# Numbers divisible by both 3 and 5
print([i for i in range(100) if i % 3 == 0 and i % 5 == 0])


# Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
c=[j for i in nested for j in i]
print(c)


# Extract unique vowels
vowel = "aeiouAEIOU"
set1 = "Programming in Python"
a = {i for i in set1 if i in vowel}
print(a)


# Convert the following list to a set using comprehension
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6]
a = {i for i in nums}
print(a)


# From the above list, create a set of their squares
num = {1, 2, 3, 4, 5, 6}
square = {i**2 for i in num}
print(square)


# Find common letters between "python" and "typhoon"
let1 ="python"
let2 = "typhoon"
simillar = {i for i in let1  for j in let2 if i== j}
print(simillar)


# extract characters that appear only once
word = "hello world"
repeat = {i for i in word if word.count(i)==(1)}
print(repeat)


# dictionary for numbers from 1 to 10 where keys are numbers and values are their squares
a = {i:i**2 for i in range(11)}
print(a)


# Count frequency of each character
word1 = "banana"
a ={i: word1.count(i) for i in word1}
print(a)


# Swap keys and values
data = {'a': 1, 'b': 2, 'c': 3}
res = {j:i for i,j in data.items()}
print(res)


# Filter by value
scores = {'Alice': 85, 'Bob': 60, 'Charlie': 90, 'David': 55}
res1 = {i:j for i,j in scores.items() if j>70}
print(res1)


# Convert two lists to dictionary
key1 = ['name', 'age', 'city']
value1 = ['John', 25, 'New York']
res = {i:j for i,j in zip(key1,value1)}
print(res)

