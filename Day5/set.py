#Create a set
set1 = {1,2,3,4,5}
print(set1)

#Create an empty set
empty1 = set()
print(type(empty1))

#Add an element
set1.add("python")
print(set1)

#Remove an element
set1.remove(3)
print(set1)

set1.discard(10)
print(set1)

#Check if 10 exists
nums = {5, 10, 15, 20}
ans = 10 in nums
print(ans)

#union
A = {1, 2, 3}
B = {3, 4, 5}
union = A | B
print(union)

#intersection
C = {10, 20, 30}
D = {20, 40, 60}
intersection = C & D
print(intersection)

#difference
E = {1, 2, 3, 4}
F ={3, 4, 5, 6}
difference1 = E - F
print(difference1)

difference2 = F - E
print(difference2)

#Create a set from a string
names = "hello" , "world"
change1 = set(names)
print(change1)

#Remove duplicates from a list
list1 = [1,"aakriti",True, 1,0,6]
set1 = set(list1)
print(set1)

#check subset
set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5,6,7}
subset1 = set1.issubset(set2)
print(subset1)

# find elements that are in either of two sets but not in both
#symmetric difference
set1 = {1,2,3,4,5,8}
set2 = {1,2,3,4,5,6,7}
result1 = set1^set2
print(result1)

#create a set of squares from 1 to 10
set_square = {}

#find all unique words using a set
sentence = "I love programming and I love python"
result = set(sentence.split())
print(result)

#checks if two strings are anagrams using sets\
word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")
output = set(word1) == set(word2)
print(output)


