"""Given an integer n. Write a program to print the last digit of n.

Examples:

Input: n = 10
Output: 0
Input: n = 9768
Output: 8
Constraints:

-109 ≤ n ≤ 109
"""
n = int(input())

# code here
last_digit=abs(n)%10
print(last_digit)
