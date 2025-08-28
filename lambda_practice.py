# lambda arguments: expression

# def square1(num):
#     return num ** 2
    
# res = square1(3)
# print(res)

# square1 = lambda num: num ** 2
# print(square1(2))


# def add (num1,num2):
#     return num1+num2

# res = add(2,5)
# print(res)

# add = lambda num1,num2 : num1+num2
# print(add(2,5))


# def check(num1):
#     if num1 % 2 == 0:
#         print("even")
        
#     else:
#         print("odd")

# res = check(13)

# check = lambda num1: "Even" if num1 % 2 == 0 else "Odd"
# print(check(2))


# square1 = lambda num: num ** 2

# a = [1,2,3,4,5]
# res = map(square1,a)
# print(list(res))




# def check(num1):
#     if num1 % 2 == 0:
#         return num1

# res = check(2)
# print(res)


# check = lambda num1: num1 % 2 == 0
# print(check(2))


# def check(num1):
#     if num1 % 2 == 0:
#         return True
#     # else:
#     return False

# a = [1,2,3,4,5]
# res = filter(check,a)
# print(list(res))



# check = lambda num1: True if num1 % 2 == 0 else False

# a = [1,2,3,4,5]
# res = filter(check,a)
# print(list(res))

from functools import reduce

# def add (num1,num2):
#     return num1+num2

# a = [1,2,3,4,5]
# res = reduce(add,a)
# print(res)


add = lambda num1,num2 : num1+num2

a = [1,2,3,4,5]
res = reduce(add,a)
print(res)