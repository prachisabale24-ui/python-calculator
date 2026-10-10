
while True:
    print("\n--- Python Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Please select 1-4.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Error! Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)
