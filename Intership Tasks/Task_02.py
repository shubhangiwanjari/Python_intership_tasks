# calculator.py Task_02

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("----- Simple Calculator -----")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Take input
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return
    
    choice = input("\nChoose operation (1/2/3/4): ")

    if choice == "1":
        print(f"\nResult: {add(num1, num2)}")
    elif choice == "2":
        print(f"\nResult: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"\nResult: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"\nResult: {divide(num1, num2)}")
    else:
        print("\nInvalid choice!")

if __name__ == "__main__":
    main()
