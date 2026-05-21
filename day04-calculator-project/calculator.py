a = int(input("enter first number:"))
operation = input("enter operation(+,-,*,/):")
b = int(input("enter second number:"))
if operation == "+":
     print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    if b == 0:
        print("Division by zero is not allowed")
    else:
        print("Result:", a / b)
else:
    print("invalid")
    