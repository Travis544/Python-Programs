num1 = float(input("enter a number:"))
op = input("enter an operator:")
num2 = float(input("enter another number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operation")
