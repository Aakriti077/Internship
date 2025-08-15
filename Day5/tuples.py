#create tuple containing five colors
colors = ("red" , "yellow" , "green" , "blue" , "white")
print(colors)

#print second and fourth color
print(colors[1])
print(colors[4])

#Create a tuple with a single element. Verify its type is tuple \
item1 = ("Hello",)
print(type(item1))

#convert list to tuple
fruits = ["apple" , "banana" , "cherry"]
changed_fruits = tuple(fruits)
print(changed_fruits)
print(type(changed_fruits))

#Concatenate two tuples
A = (1,2,3)
B = (4,5,6)
A += B
print(A)


#Check whether "python" exists in the tuple
language = ("java", "python", "c++")
# find = "python"
print("python" in language)


#unpack variables
nums = (10, 20, 30, 40)
(firstnum , secondnum , thirdnum , lastnum) = nums
print(firstnum)
print(secondnum)
print(thirdnum)
print(lastnum)

#finding index
numbers = (1,5,7,5,9)
index1 = numbers.index(5)
print(index1)

#slicing tuple
t = ("a", "b", "c", "d", "e")
slice1 = t[1:4]
print(slice1)

#Count how many times 2 appears
number2 = (2, 4, 2, 6, 2, 8)
count1 = number2.count(2)
print(count1)

#Merge two tuples and sort them into a new tuple.

#list ma convert garera sort garni
#merging tuples
first_name = ("Aakriti",)
last_name = ("Acharya",)
full_name = first_name+last_name

list1 = list(full_name)  #convert to list 

#sorted the list the convert to tuple
list1.sort()
new_tuple = tuple(list1)
print(new_tuple)


#remove an element from tuple
names = ("Ram" , "Hari" , "Shyam" , "Aakriti")
new_list = list(names)
new_list.remove("Aakriti")
new_names = tuple(new_list)
print(new_names)

#convert to dictionary
t = (("a", 1), ("b", 2), ("c", 3))
new_t = dict(t)
print(new_t)

#Swap two tuples
t1 = (1,2)
t2 = (3,4)
swap = t1, t2 = t2, t1
print(swap)

#reverse
input1 = ("happy" , "sad", "angry")
final = tuple(reversed(input1))
print(final)

#Create a tuple from user input where values are comma-separated
text = input("Enter your tuple: ")
a=tuple(text)
print(a)
