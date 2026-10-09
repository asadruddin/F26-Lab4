# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: ayaan sadruddin
# Date: 9 oct 2026
# Purpose: Create the complete calculator function using default parameters and positional parameters
# Usage: ./lab4d.py
def compute(num1, num2, operations='+'):
     if operations=='+':
        return num1+num2
     elif operations=='-':
        return num1-num2
     elif operations=='*':
        return num1*num2
     elif operations=='/':
        return num1/num2
def main():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    operations=input("choose operations (+, -, *, /): ")
    result=compute(num1, num2, operations)
    print("result:", result)
    print(compute(13,45,'*'))
    print(compute(13,45,'/'))
    print(compute(13,45,'-'))
    print(compute(13,45,'+'))
    print(compute(13,45))
if __name__=="__main__":
    main()
