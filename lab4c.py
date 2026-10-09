# Add comments before you do anything else.
#!/usr/bin/env python3
# Author:
# Date:
# Purpose: use the main Function as entry point.
# Usage: ./lab4c.py
def sum(num1, num2):
    return num1 + num2
def main():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    result=sum(num1, num2)
    print("the sum is:",result)
if __name__=="__main__":
    main()