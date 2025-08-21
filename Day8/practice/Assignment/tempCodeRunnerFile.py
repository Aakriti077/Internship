#Create a text file named data.txt and write the following lines
# with open("data.txt", "w") as f:
#     f.write("Python is fun.\n")
#     f.write("File handling makes it powerful.\n")
#     f.write("Exception handling makes it reliable.\n")


# #read the entire contents of data.txt and display it on the screen. 
# with open("data.txt", "r") as f:
#     f_content = f.read()
#     print(f_content)

# #to read only the first 10 characters from data.txt 
# with open("data.txt","r") as f:
#     f_content = f.read(10)
#     print(f_content)

# #Use .readline() to read the first line only
# with open("data.txt","r") as f:
#     f_content = f.readline()
#     print(f_content)


# #Use a loop with .readline() or .readlines() to display all lines one by one.
# with open("data.txt","r") as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)

#     while len(f_contents) > 0:    
#         print(f_contents, end="*")
#         f_contents = f.read(size_to_read)


# #Write a program that takes user input and appends it to data.txt without overwriting existing content
# with open("data.txt","r") as ff:
#     user1 = input("Enter your desired text: ")
#     with open("data.txt","a") as f:
#         f_contents = f.write(user1)

# # program that creates another file named copy.txt and copies all content from data.txt into it
# with open("data.txt","r") as f:
#     f_content = f.read()
#     with open("copy.txt","w") as w:
#         w_content = w.write(f_content)


# #program to count the number of words in data.txt 
# with open("data.txt","r") as f:
#     f_content = f.read()
#     words = f_content.split()
#     word_count = len(words)
#     print(word_count)

# # #program to find and print the longest word in data.txt 
# with open("data.txt","r") as f:
#     f_content = f.read()
#     words = f_content.split()
#     length1 = (max(words, key=len))
#     print(f"The longest word is: {length1}")
#     # word1 = len(length1)
#     # print(f"The number of words is: {word1}")