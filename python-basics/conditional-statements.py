num_str=input("Hi what is your name ?")
age=int(input("Hi "+num_str+", What is your age?"))

password='123123123'

if password=="secreate@123":
    print("Access Granted")
else:
    print("Access Denied")

if age>=18:
    print("You are a adult")
    print("You can vote")

else:
    print("You are a baccha")
    print("Go have some ice cream")


#if elif statement
score=85

if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='F'

print("Your grade is:",grade)

#Nested if else

age=25
has_license=True

if age>=18:
    print("Your are old enough to drive")

    if has_license:
        print("You can Drive!")
    
    else:
        print("You need a License")

else:
    print("Too Young to Drive")


# if-else using AND condition

age=20
has_ticket=True

if age>=18 and has_ticket:
    print("You can enter the concert")

else:
    print("Cannot enter")

#if-else using OR statement

day="Saturday"

if day=="Sunday" or day=="Saturady":
    print("It is a weekend")

else:
    print("It is a weekday")

#if-else using Not

is_sunny=True

if not is_sunny:
    print("its Sunny")
else:
    print("its cloudy")

#Ternary Operator

status='adlut' if age>=18 else 'minor'
print(status)