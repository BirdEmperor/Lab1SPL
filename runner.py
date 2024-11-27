from Classes.calculator import Calculator
from __init__ import memory, history
from settings import decimal_places
# Input validation for numbers
def get_number(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'm' and memory is not None:
            return memory
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'm' to use the stored memory value.")

# Input validation for operator
def get_operator():
    while True:
        operator = input("Choose an operator (1 for +, 2 for -, 3 for *, 4 for /, 5 for ^, 6 for %, 7 for √): ").strip()
        if operator in {'1', '2', '3', '4', '5', '6', '7'}:
            return int(operator)
        else:
            print("Invalid operator. Please enter a valid one.")

# Main calculator loop
def main():
    global memory, decimal_places
    calc = Calculator
    
    while True:
        # Get numbers and operator with validation
        num1 = get_number("Enter the first number (or 'm' for memory): ")
        operator = get_operator()
        
        # Square root only needs one number
        if operator == 7:  # Square root
            result, operation_symbol = calc.calculate(num1, None, operator)
            operation_str = f"√{num1}"
        else:
            num2 = get_number("Enter the second number (or 'm' for memory): ")
            result, operation_symbol = calc.calculate(num1, num2, operator)
            operation_str = f"{num1} {operation_symbol} {num2}"

        # Display result with conditional formatting
        if isinstance(result, str):
            print(result)  # Show error messages
        else:
            # Conditional display format for integers vs floats
            if result.is_integer():
                result = int(result)  # Convert to int if result is a whole number
            else:
                result = round(result, decimal_places)  # Format with decimals if not integer
            print(f"Result: {result}")
            history.append(f"{operation_str} = {result}")
        
        # Memory options
        memory_option = input("Do you want to store this result in memory? (y/n): ").strip().lower()
        if memory_option == 'y':
            memory = result

        # Show history
        history_option = input("Do you want to view calculation history? (y/n): ").strip().lower()
        if history_option == 'y':
            calc.show_history()
        
        # Settings adjustment
        settings_option = input("Do you want to change calculator settings? (y/n): ").strip().lower()
        if settings_option == 'y':
            try:
                decimal_places = int(input("Enter the number of decimal places for results: ").strip())
                print(f"Decimal places set to {decimal_places}.")
            except ValueError:
                print("Invalid input. Decimal places will remain unchanged.")

        # Repeat or exit
        repeat = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Exiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
