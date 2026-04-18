#!/usr/bin/python3
x = ""
def print_last_digit(number):
    if number < 0:
      number = - number
    x = x + number % 10
    return x
