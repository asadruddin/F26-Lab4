# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ayaan sadruddin
# Date: 9 oct 2026
# Purpose: Create Simple Functions.
# Usage: ./lab4a.py
# TO DO 1: Add the docstring
# TO DO 2: define the function with name `is_even`.
def is_even(mylist):
    found = False
    for number in mylist:
        if number % 2 == 0:
            return True
            break
    return False
numbers=[1,3,5,7,8,9]
result=is_even(numbers)
print(result)

