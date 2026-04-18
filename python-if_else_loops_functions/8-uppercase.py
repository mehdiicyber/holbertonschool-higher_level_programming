#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            print("{}".format(i.upper()))
        else:
            print("{}".format(i), end = "")
            
  
