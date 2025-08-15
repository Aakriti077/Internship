#Create a dictionary
dictionary1 = {"name":"Aakriti","age":21,"city":"Kathmandu"}
print(dictionary1)

#accessing value
information = {"name": "John", "age": 25, "city": "London"}

i1 = information["age"]
print(i1)

information["country"]= "UK"  #add country uk 
print(information)

information["city"]= "Paris"  #change city 
print(information)

information.pop("age")
print(information)

#Check if the key "salary" exists
names = {"name": "Sam", "salary": 5000}
print("salary" in names)

#Merge two dictionaries
first = {1: "a", 2: "b"}
second = {3: "c", 4: "d"}
result = first | second
print(result)

#Get all keys and all values separately
print(first.keys())
print(second.values())

#Create a dictionary from two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict1 = zip(keys,values)
result = dict(dict1)
print(result)

#Count how many times each letter appears
letters = "banana"
letter1 = dict()
letter1["b"]=letters.count("b")
letter1["a"]=letters.count("a")
letter1["n"]=letters.count("n")
print(letter1)


my_dict = {"apple":1, "banana":2, "cherry":3}
value1 = max(my_dict)
print(value1)













