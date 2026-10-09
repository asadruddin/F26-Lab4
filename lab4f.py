# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice variable number of arguments with *args
# Usage: ./lab4f.py
def get_initials(*args):
    initials=[]
    for name in args:
        initials.append(name[0])
    return initials 
print(get_initials("alex","sandra","billy"))
