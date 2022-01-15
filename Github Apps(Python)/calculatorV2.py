def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enther the second number: "))
    op = input("Now enter the operator: ")

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num2 - num1)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else: 
        print("\nInvalid Operator!")
    
calculator()

