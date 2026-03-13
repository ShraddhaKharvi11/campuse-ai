
#import os
#with open("Book2.csv","r") as file:
#    for line in file:
#        data=line.strip().split(",")
#        #print(data)
#        print("Dear", data[1],", Your user ID is ",data[0])
#       response=os.system("ping -c 1 "+data[3])

#with open("students.csv","w") as file:
#   file.write("name,age,grade\n")
#    file.write("Shraddha,21,A\n")
#    file.write("Shreya,22.A\n")

import csv
#students=[
#["name","age","grade"],
#["Shraddha",21,"A"],
#["Shreya",22,"A"]
#]
#with open("new-student.csv","w",newline='')as file:
# writer=csv.writer(file)
# writer.writerows(students)


with open("new-student.csv",'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)