#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value: The value to print (can be any type).

    Returns:
        True if value was correctly printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
