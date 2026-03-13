#file=open("test.txt",'r')
#content=file.read()
#print(content)
#file.close()

#with open("test.txt","r") as file:
#    content=file.read()
#    print(content)   # with using this no need to close file

#print("\n")

#with open("test.txt","r") as file:
#    line=file.readline()
#    print(line)

#print("\n Different")

#with open("test.txt",'r')as file:
#    lines=file.readlines()
#    for line in lines:
#        print(line.strip())

#with open("output.txt",'w')as file:
#    file.write("Hello world1\n")
#    file.write("This is a new file\n")

#with open("output.txt",'a')as file:
#    file.write("Hello world1\n")
#    file.write("This is a new file\n")

try:
    with open("students_new","r") as file:
        content=file.read()

except FileNotFoundError:
    print("File Not Found")

except PermissionError:
    print("You don't have permission to access this files")
except Exception as e:
    print(f"An Error occured:{e}")