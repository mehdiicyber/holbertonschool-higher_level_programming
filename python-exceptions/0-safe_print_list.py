#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Siyahıdakı x qədər elementi çap edən funksiya.

    Args:
        my_list: Çap ediləcək elementlərin siyahısı.
        x: Çap ediləcək elementlərin sayı.

    Returns:
        Çap olunmuş elementlərin real sayı.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
