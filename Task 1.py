'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

'''
# Code Starts from here..
number = int(input("Enter the number : "))
if(number%2==0 or number==0):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
print("Thank You !!!")
# Code ends here .