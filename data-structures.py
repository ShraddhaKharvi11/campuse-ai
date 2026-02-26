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
#Dictionaries
#Sets