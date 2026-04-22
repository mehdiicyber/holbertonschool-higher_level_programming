#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Print the integer. Use end=" " to keep them on the same line.
            # We use a condition to avoid a trailing space at the end of the row.
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        # After the inner loop finishes a row, print a newline
        print()
