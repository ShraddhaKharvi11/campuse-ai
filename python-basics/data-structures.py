#Lists

students=['Shraddha','swamya','Manjunatha','Kavya']
numbers=[23,56,3,4,89,4]
mixed=['Kharvi',20,True]
print(students[1:4])
print(mixed[-1])
print(students[::2])

students[1]="Arun"
print(students[1])
print(students)
students.remove("Arun")
print(students)

#Length
print("Length of students in a students list",len(students))
#sum,min,max
print("Sum of all number in a number list",sum(numbers))
print("Minimum number in the number list",min(numbers))
print("Maxmium number in the list ",max(numbers))
#count
print("Total number of occurances of number 4 in a list",numbers.count(4))
#fint index
print("The index of the list item Manjunath is",students.index("Manjunatha"))
#sort
numbers.sort()
print(numbers)
students.sort()
print(students)
#reverse
numbers.reverse()
print(numbers)
#Check Membership
print("Manjunatha" in students)

for name in students:
    print(name)
print(range(len(students)))

for i in range(len(students)):
    print(f"{i} : {students[i]}")

print(enumerate(students))

for k,v in enumerate(students):
    print(f"{k} : {v}")

#List comprehension
#squares=[]

#for i in range(1,6):
#    squares.append(i**2)
#print(squares)

squares=[i**2 for i in range(1,6)]
print(squares)

#Tuples
# It is immutable
coorinates=(10,20)
person=("Kavya",21,"Chitradurga")
print(person[2])

name,age,district=person

print(f"I am {name}, from {district},I am {age} years old")
#Dictionaries
mathClass={}
student={"name":"Shraddha","age":25,"grade":"A",
         "course":["Math","Science","Social science"],}
#print(student["name"])
#print(student.get("phone"))
#print(student.get("phone","User's phone number doesn't exists"))
student['phone']='8967543567'
#print(student.get("phone","User's phone number doesn't exists"))
student['age']=26
#print(student)

#student.pop('grade')
#print(student)

#for key in student:
#    print(f"{key}:{student[key]}")

for key,value in student.items():
    print(f"{key}:{value}")

#Sets

empty_set=set()

numbers=[1,2,3,4,88,99,22,2,3,44,33,22,44,99,1,5,5,4,6]
unique_number=set(numbers)

print(numbers)
print(unique_number)

unique_number.add(100)
unique_number.discard(88)
print(unique_number)