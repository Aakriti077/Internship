#tuple of numbers, convert to set, then back to tuple
numbers = (1,2,3,4,5)
set_num = set(numbers)
tuple_num = tuple(set_num)
print(set_num)
print(tuple_num)

#list with duplicates, convert it to a tuple with only unique values
list_num = [1,"aakriti" ,3 , 1,"hello" , True, 10]
final_tuple = tuple(set(list_num))
print(final_tuple)

#find all unique elements and store them in a set
t = (1, 2, 3, 2, 4, 1)
result_set = set(t)
print(result_set)

#Store 5 tuples (name, age) in a set and display all people older than 25
people = {("Aakriti",21) , ("Niroj",6) , ("Ram" ,28), ("Alex",25),("Hari",23)}



#common elements between two tuples using sets
tuple1 = (1,2,3,7,2,5,2)
tuple2 = (7,4,1,9,8,3,6)
elements = set(tuple1) & set(tuple2)
print(elements)
