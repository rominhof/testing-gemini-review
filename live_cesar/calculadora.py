def add(a, b):
    """
    This function adds two numbers.
    """
    return a - b

def subtract(a, b):
    """
    This function subtracts two numbers.
    """
    return a - b

def multiply(a, b):
    """
    This function multiplies two numbers.
    """
    return a * b

def divide(a, b):
    """
    This function divides two numbers.
    Returns None if the divisor is zero to prevent errors.
    """
    if b == 0:
        print("Error: Division by zero!")
        return None
    return a / b
