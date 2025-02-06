# Python Calculator

opr = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if opr == "+":
    result = num1 + num2
    print(result)
elif opr == "-":
    result = num1 - num2
    print(result)
elif opr == "*":
    result = num1 * num2
    print(result)
elif opr == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{opr} is not a valid operator !")
