
print("I am Shraddha")


def iAMGroo():
    print("I am Groot")

for i in range (5):
    iAMGroo()

#functions with Arguments/parameters and Return Types
#functions with no Arguments/Parameters and only return types
#functions with Arguments/Parameter and no return type
#functions with no arguments/parameter and no retuen types


#name=input("Enter your name")
def greet_someone(name):
    print(f"Hello,{name}")
    print("Welcome to my Python Script")

#greet_someone(name)

def sum(a,b):
    result=a+b
    print(f"Sum {a} + {b} = {result}")

sum(3,4)

def mul(a,b):
    """
    This ifunction is used to calcualte 2 number multiplication

    Parameters:
    a(int):First variable
    b(int):Second variable

    Returns:
    int: The multiplication of 2 number
    """
    results= a*b
    return results

#a=int(input("enter the value for a "))
#b=int(input("Enter the value for b "))

#help(mul)

#print(f"Multiplication of {a} * {b} =",mul(a,b))

def sum(*args):
    result=0
    for num in args:
        result+=num
    return result

#a=int(input("enter the value for a "))
#b=int(input("Enter the value for b "))
#c=int(input("enter the value for c "))
#d=int(input("enter the value for d "))
#e=int(input("enter the value for d "))


#print(f"Sum of {a} + {b} =",sum(a,b,c,d,e))

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_info(name="Sharddha",age=21)


