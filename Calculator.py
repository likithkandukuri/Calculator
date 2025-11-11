import math

print("\nWelcome to the Advanced Calculator\n")

# Function to handle "continue?" prompt reliably
def ask_continue():
    while True:
        user_continue = input("Want to continue? Yes [y] or No [n]: ").strip().lower()
        if user_continue in ['y', 'yes']:
            return True
        elif user_continue in ['n', 'no']:
            return False
        else:
            print("Invalid input! Please type 'y' or 'n'.")


# Function for Addition
def addition(value, history):
    result = value
    while True:
        try:
            add_input = float(input("\nEnter a number to add: "))
            result += add_input
            result = round(result, 4)
            print(f"Current Result: {result}")
            history.append(f"Added {add_input} → Result = {result}")
            if not ask_continue():
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return result


# Function for Subtraction
def subtraction(value, history):
    result = value
    while True:
        try:
            sub_input = float(input("\nEnter a number to subtract: "))
            result -= sub_input
            result = round(result, 4)
            print(f"Current Result: {result}")
            history.append(f"Subtracted {sub_input} → Result = {result}")
            if not ask_continue():
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return result


# Function for Multiplication
def multiplication(value, history):
    result = value
    while True:
        try:
            mul_input = float(input("\nEnter a number to multiply: "))
            result *= mul_input
            result = round(result, 4)
            print(f"Current Result: {result}")
            history.append(f"Multiplied by {mul_input} → Result = {result}")
            if not ask_continue():
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return result


# Function for Division
def division(value, history):
    result = value
    while True:
        try:
            div_input = float(input("\nEnter a number to divide: "))
            if div_input == 0:
                print("Can't divide by zero! Try again.")
                continue
            result /= div_input
            result = round(result, 4)
            print(f"Current Result: {result}")
            history.append(f"Divided by {div_input} → Result = {result}")
            if not ask_continue():
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return result


# Function for Percentage
def percentage(value, history):
    result = value
    while True:
        try:
            per_input = float(input("\nEnter the percentage value: "))
            result = round(result * (per_input / 100), 4)
            print(f"{per_input}% of previous value = {result}")
            history.append(f"Calculated {per_input}% → Result = {result}")
            if not ask_continue():
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return result


# Function for Power
def power(value, history):
    try:
        pow_input = float(input("\nEnter the power/exponent: "))
        result = round(value ** pow_input, 4)
        print(f"{value} ^ {pow_input} = {result}")
        history.append(f"Raised {value} to {pow_input} → Result = {result}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        result = value
    return result


# Function to View History
def show_history(history):
    print("\nOperation History:")
    if not history:
        print("No operations performed yet.")
    else:
        for i, entry in enumerate(history, start=1):
            print(f"{i}. {entry}")
    print("-" * 40)


# Function to Exit Program
def clear():
    print("\nThank you for using the calculator! Goodbye.")
    quit()


# Main Function
def main():
    history = []

    while True:
        try:
            number_input = float(input("Enter the starting number: "))
            break
        except ValueError:
            print("Invalid input! Please try again.")

    while True:
        print("\n" + "-" * 40)
        print(f"Current Number: {number_input}")
        print("""
Functions: 
  1. Addition
  2. Subtraction
  3. Multiplication
  4. Division
  5. Percentage
  6. Power
  7. View History
  8. Clear (Exit)
        """)
        user_input = input("Your choice: ").strip()

        if user_input == "1":
            number_input = addition(number_input, history)
        elif user_input == "2":
            number_input = subtraction(number_input, history)
        elif user_input == "3":
            number_input = multiplication(number_input, history)
        elif user_input == "4":
            number_input = division(number_input, history)
        elif user_input == "5":
            number_input = percentage(number_input, history)
        elif user_input == "6":
            number_input = power(number_input, history)
        elif user_input == "7":
            show_history(history)
        elif user_input == "8":
            clear()
        else:
            print("Invalid choice! Please try again.")


# Run the Program
if __name__ == "__main__":
    main()
