'''
Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

'''
# Code start from here...
l=list(range(1,51))
sum = 0
for i in l:
   sum = sum + i
print(f"The sum of the numbers from {l[0]} to {l[51-2]} is : {sum}")
# Code ends here..

