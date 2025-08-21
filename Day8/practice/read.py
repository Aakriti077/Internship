# f = open("example.txt", "r")  #open file in specific mode
# print(f.name)

# f.close()  # close file

# print(f.mode) #which mode file is open

# print(f.closed)  #check if file is closed or not

# with open("example.txt","r") as f:  #with open use garyo vani file affai close hunxa close garna pardaina
#     print(f.name)
#     print(f.closed)
#     print(f.mode)

# print(f.closed)

with open("example.txt","r") as f:
    # f_contents = f.read() #read whole file
    # f_contents = f.readline() #read one line
    # f_contents = f.readlines() #read whole line and return in 

    # f_contents = f.readline()
    # print(f_contents)
    # f_contents = f.readline()  #2 lines print hunxa 
    # print(f_contents)

    # for line in f:
    #     print(line)  #print all lines with loop

    # f_contents = f.read(100)  #read 100 characters
    # print(f_contents)

    # f_contents = f.read(10)  #read 10 characters
    # print(f_contents)
    
    # f_contents = f.read(10)  
    # print(f_contents)
    # f_contents = f.read(10)   #multiple garda 10 ota print vayera next line ma print hucha
    # print(f_contents)
    # f_contents = f.read(10)  
    # print(f_contents)

    # print("Cursor is in the line: ",f.tell())
    # size_to_read = 99
    # f_contents = f.read(size_to_read)
    # print("Cursor is in the line: ",f.tell())    #tell le cursor to point kata xa dinxa

    # while len(f_contents) > 0:    #100 ota line lidai words nasakiye samma chaliranxa
    #     print(f_contents, end="*")
    #     f_contents = f.read(size_to_read)  


    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents)
    f.seek(0)  #same content feri print garxa
    f_contents = f.read(size_to_read)
    print(f_contents)

    

