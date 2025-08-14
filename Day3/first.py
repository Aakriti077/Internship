#Part-1

#Length and Indexing

#Store your favorite quote in a variable.
message = "Dream big, start small, act now"

#Print its length
print(len(message))

#Print the first character
print(message[0])

#Print the last characters
print(message[-1])

#Concatenation

#Store first and last name in seperate variables
a = "Aakriti"
b = "Acharya"

#Combining into one string with space in between
print(a+ " "+b)

#Repetiotion

#Print "Python!" 10 times in a single line.
a = "Python!"
print(a *10)

#Part 2
 
#String Methods
learn = "learning python"

#Converting to all uppercase
print(learn.upper())

#Converting to all lowercase
print(learn.lower())

#Converting to title case
print(learn.title())

#Remove spaces from " Clean me "
b=" Clean me " 
print(b.strip())

#Replace "dog" with "cat" in "I have a dog"
m = "I have a dog"
n = m.replace ("dog", "cat")
print(n)

#Count how many times "a" appears in "Banana" 
c = "banana"
print(c.count("a"))


#Slicing and Substrings

#Extract "thon" from "Python"
word = "Python"
print(word[2:])

#From "I love programming" , extract "love" 
word = "I love programming"
print(word[2:6])

#Reverse the string "Python" using slicing
s = "Python"
print(s[::-1])

#Escape Characters

#Print using \n
word = "nginx \nCopyEdit \nHello \nWorld"
print(word)

words = "makefile \nCopyEdit \nName: John \nAge: 25"
print(words)

#Searching

#Check if pyhton is present in given string
w = "I love Python programming"
print("Python" in w)

#Find index of "code" in "Let's code in python"
word = "Let's code in python"
print(word.index("code"))

#Formatting

#Using f-string
a = "Alice"
b = 20
print(f"My name is {a} and I am {b} years old")

#using .format()
a= 30 
b="°C"
print("Temperature today is {}{}".format(a,b))

#Taking string from user and:
  #Print in reverse

name = input("Enter your name: ")
print(f"My name is {name[::-1]}")

#Check if string is a palindrome (same forward and backward)

word = input("Enter your word: ")
if word ==  word[::-1]:
    print(f"'{word}' is palindrome")
else:
    print(f"'{word}' is not palindrome")


#Count number of words
text = input("Write your sentence: ")
print(f"The number of word is: '{len(text.split())}'")

#Replace vowels with "*"

a = input("Write your sentence: ")
a = a.replace("a" , "*")
a = a.replace("e" , "*")
a = a.replace("i" , "*")
a = a.replace("o" , "*")
a = a.replace("u" , "*")
print(a)





# b = ["a","e","i","o","u"]
# for i in b:
#     a = a.replace(i , "*")
# print(a)

#Abbreviation Maker
word = input("enter a sentence to create: ")
a = word.split()
b = ""
for i in a:
    b += i[0]
print(b)

#Word Replacer
a = input("Enter your sentence: ")
b = input("Enter word you want to replace: ")
c = input("Enter your replaced word: ")
d = a.replace(b,c)
print("Replaced word: ", d)

#username generator
firstname = input("Enter your First Name: ")
lastname = input("Enter your Last Name: ")
birthdate = input("Enter your Birth Date: ")
name = firstname.lower() + lastname.lower() + birthdate
print(f"The username is: {name}")

#password generator
import random

random1 = random.randint(1, 10)
word = input("Enter your desired word: ")
word1 = word[::-1] + word.upper() + str(random1)
print(word1)

#Pig latin
word = input("Enter your word: ")
a = word[1:] + word [0] + "ay"
print(a)









