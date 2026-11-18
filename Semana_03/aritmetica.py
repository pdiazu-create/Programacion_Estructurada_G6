"""operaciones basicas:
suma, resta, multiplicacion y division
"""
def add(number1, number2):
    return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mult(number1, number2):
    return number1 * number2

def div(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input. Please provide numeric values."