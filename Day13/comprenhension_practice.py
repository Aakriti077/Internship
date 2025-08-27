# numbers = [1,2,3,4,5]
# num2 = []
# for i in numbers:
#     num2.append(i ** 2)

# print(num2)

#expression = kun operation garni

# numbers = [1,2,3,4,5]
# print([i*i for i in numbers])

# numbers = [1,2,3,4,5]
# num2 = []
# for i in numbers:
#     if i % 2 == 0:
#         num2.append(i ** 2)
# print(num2)

# numbers = [1,2,3,4,5]
# print([i**2 for i in numbers if i %2 == 0])


# numbers = [1,2,3,4,5]
# num2 = []
# for i in numbers:
#     if i % 2 == 0:
#         num2.append("even")
#     else:
#         num2.append("odd")
# print(num2)


# numbers = [1,2,3,4,5]
# print(["Even" if i % 2== 0 else "Odd" for i in numbers])

# numbers = [1,2,3,4,5]
# print({i*i for i in numbers})

# numbers = [1,2,3,4,5]
# print({i**2 for i in numbers if i %2 == 0})


# numbers = [1,2,3,4,5]
# print({"Odd" if i % 2== 0 else "Even" for i in numbers})


# result = {}
# for i in range(5):
#         result[i] = i**2
# print(result)


print({i**2:i for i in range(5) })
