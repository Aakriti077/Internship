#Handle ZeroDivisionError
try:
    num = int(input("Enter a number: "))
    result1 = 100 / num
    print(f"Result: {result1}")

except ZeroDivisionError:
    print("Cannot divide by 0!")


#Handle FileNotFoundError
try:
    with open("missing.txt","r") as f:
        f_content = f.read()
        print("File found!")
except FileNotFoundError:
    print("File was not found!")


#Handle ValueError
try:
    num = int(input("Enter a num: "))
    print(f"Num is: {num}")
except ValueError:
    print("Invalid input!")

#Ask the user to enter a filename.then try to open and read the file. If the file doesn’t exist, print a message
message = input("Enter a message: ")
try:
    with open(message,"r") as f:
        f_content = f.read()
        print("File has: ")
        print(f_content)
except FileNotFoundError:
    print("File not found. Please check the filename.")

try:
    with open("datas.txt","r") as f:
        f_content = f.read()
        print(f"File content: {f_content}")
except FileNotFoundError:
    print("The file does not exist")
finally:
    print("File is here")
