import math
from settings import decimal_places
from __init__ import memory, history

class Calculator:
    
    def show_history():
        if history:
            print("\nCalculation history:")
            for entry in history:
                print(entry)
        else:
            print("No calculations yet.")
    
    # Function for calculator operations
    def calculate(num1, num2, operator):
        match operator:
            case 1:  # Addition
                return num1 + num2, '+'
            case 2:  # Subtraction
                return num1 - num2, '-'
            case 3:  # Multiplication
                return num1 * num2, '*'
            case 4:  # Division
                if num2 != 0:
                    return num1 / num2, '/'
                else:
                    return "Error: Division by zero!", None
            case 5:  # Exponentiation
                return num1 ** num2, '^'
            case 6:  # Modulo
                return num1 % num2, '%'
            case 7:  # Square root
                return math.sqrt(num1), '√'
            case _:
                return "Error: Invalid operator!", None