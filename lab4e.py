# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Modify the calcualtor program to use keyword parameters.
# Usage: ./lab4e.py
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
    result=compute(num1=num1, num2=num2, operations=operations)
    print("result:", result)
    print(compute(num1=13,num2=45,operations='*'))
    print(compute(num1=13,num2=45,operations='/'))
    print(compute(num1=13,num2=45,operations='-'))
    print(compute(num1=13,num2=45,operations='+'))
    print(compute(num1=13,num2=45))
if __name__=="__main__":
    main()


