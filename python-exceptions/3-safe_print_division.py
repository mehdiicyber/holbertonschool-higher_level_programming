#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result in the finally block.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        The result of the division, or None if division by zero occurs.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
