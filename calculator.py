a=float(input("enter first number:\n"))
b=float(input("enter second number:\n"))
 
def addition():
    print(f"({a})+({b})={a+b}")
def minus():
    print(f"({a})-({b})={a-b}")
def multiplication():
    print(f"({a})x({b})={a*b}")
def division():
    print(f"({a})/({b})={a/b}")

add = "+"
subtract = "-"
divide = "/"
multiply = "x"

operation = input("/,+,-,x\nFrom above Please enter the operation you want to perforn on two numbers:\n")

if(operation==add):
   addition()
        
elif(operation==subtract):
     minus()

elif(operation==divide):
    division()

if(operation==multiply):
    multiplication()   