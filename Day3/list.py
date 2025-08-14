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
list = ["apple" , "samsung" , "redmi"]
print(list*3)

print("apple" in list) #check if apple exist in list using in operator





