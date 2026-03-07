#count=0

#while count<=10:
#    print("Count is",count)
#    count+=1
#print("Done!")

#for loop

count=0
for count in range(count,10):
    print(count)
    


for i in range(1,10):
    for j in range(i):
        print("*",end=' ')

    print()  

#Loops with Conditional statements

numbers=[1,2,3,4,5,6,7,8,9]

search_for=6

for num in numbers:
    if num==search_for:
        print("Found it")
        break
else:
    print("Not found")
