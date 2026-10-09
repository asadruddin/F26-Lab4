# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:ayaan sadruddin
# Date: 9 oct 2026
# TO DO 1: Add the docstring
# TO DO 2: Create the function.
# TO DO 3: Call the function.
def even_numbers(mylist):
    even_list=[]
    for number in mylist:
        if number % 2==0:
            even_list.append(number)
    return even_list
numbers=[1,2,3,4,5,6,7,8]
result=even_numbers(numbers)
print(result)
