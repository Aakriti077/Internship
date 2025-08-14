#Create list with 5 fav movies

movie = ["Ballarina" , "Housefull" , "Titanic" , "Scream" , "Avatar" ]
print(movie)

#Create list with mixed data types
data = [7 , "aakriti" , 50.0 , True]
print(data)

#Creating nested list
nested_list = ["C#" , "Java" , ["python" , "django" ] , "Ruby"]
print(nested_list)

#access the first emement of list
items = ["apple" , "banana" , "cherry" , "grapes" , "mango"]
print(items[0])

#access the middle emement of list
items = ["apple" , "banana" , "cherry" , "grapes" , "mango"]
print(items[:-1])

#access last element of list
items = ["apple" , "banana" , "cherry" , "grapes" , "mango" , "orange"]
print(items[-1])

print(items[-2]) #use negative indexing to get second last element

print(items[0:3]) #print first 3 element of list using slicing

print(items[-3:]) #print last 3 element of list using slicing

print(items[::-1]) #reverse list using slicing

#replace second element with python
elements = ["C#" , "Java" , "swift" , "django"  , "Ruby"]
elements[1] = "python"
print(elements)

elements[3:5] = "done" , "finish"  #replace last two elements
print(elements)

#concatenate two lists
list1 = ["dog" , "cat" , "deer" , "elephant"]
list2 = ["fish" , "frog" , "snake"]
print(list1+list2)

#repeat list 3 times
list1 = ["apple" , "samsung" , "redmi"]
print(list1*3)

print("apple" in list1) #check if apple exist in list using in operator

#list methods

numbers = [5,2,9,1,5,6]
fruits = ["apple" , "banana" , "cherry"]
fruits.append("orange")     #Append
print(fruits)


fruits.insert(1, "kiwi")     #Insert
print(fruits)

fruits.remove("banana")     #Remove
print(fruits)

numbers.pop(5)
print(numbers)

fruit = ["apple" , "banana" , "cherry"] #clear all elements from fruit
fruit.clear()
print(fruit)

numbers.sort()      #sorts in ascending order
print(numbers)

numbers.sort(reverse=True)      #reverse in descending order
print(numbers)

fruits.reverse()    #reverses list
print(fruits)

fruits.sort()       #sorts in alphabetical order
print(fruits)

x= numbers.count(5)     #count number of 5
print(x)

x = fruits.index("cherry")      #check which index cherry is in
print(x)

#shallow copy - numbers are immutable so changes in b wont change a in shallow copy
import copy  
numbers = [5,2,9,1,5,6]
b = copy.copy(numbers)
b[2] = 7
print(numbers)
print(b)

#Mini task
 
numbers = [1,2,3,4,5,6,7,8,9,10]
max_num = max(numbers)
print(max_num)

min_num = min(numbers)
print(min_num)

sum1 = sum(numbers)
print(sum1)

#all ma all value true vayo vani true hunxa else false(euta matra false vayo vani false )
list1 = ["apple" , 2 , 5, "banana" , 10 , True, -2]
check_all = all(list1)
print(check_all)

#any ma any one value true vayo vani true hunxa else false (empty vayo vani)
list1 = [0 , 1]
check_any = any(list1)
print(check_any)

list1 = ["aakriti" , 2 , True , "hello" , 90.0]
length = len(list1)
print(length)

fruit = "apple"
a = list(fruit)
print(a)

b = list(range(1,5))
print(b)






