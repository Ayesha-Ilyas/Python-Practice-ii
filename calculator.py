num1=input("enter a number:  ")
num2=input("enter a number:  ")
op=input("enter a operator:  ")
def max_no(num1,num2):
    if   op =="+":
       print(num1 + num2)
    elif op =="*":
       print(num1 * num2)
    elif op == "/":
       print(num1 / num2)
    elif op == "-":
       print(num1 - num2)
    elif op == "%":
       print(num1 % num2)
    else:
       print("invalid operator")
max_no(int(num1),int(num2))
