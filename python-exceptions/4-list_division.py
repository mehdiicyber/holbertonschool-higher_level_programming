#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists up to a specified length.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list of length list_length containing the division results.
    """
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]
            div_result = val_1 / val_2
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_result)
    return new_list
