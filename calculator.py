def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        result = num1 + num2
        operation = "addition"
    elif choice == '2':
        result = num1 - num2
        operation = "subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "multiplication"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "division"
        else:
            print("Error! Division by zero.")
            return
    else:
        print("Invalid input! Please enter a valid choice.")
        return
    
    print(f"The result of the {operation} is: {result}")

calculator()
