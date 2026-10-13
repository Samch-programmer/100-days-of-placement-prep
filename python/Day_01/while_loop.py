"""Given a number x, print the numbers from x to 0 in decreasing order in a single line.

Examples:

Input: x = 3
Output: 3 2 1 0
Explanation: Numbers in decreasing order from 3 are 3 2 1 0.
Input: x = 5
Output: 5 4 3 2 1 0
Explanation: Numbers in decreasing order from 5 are 5 4 3 2 1 0.
Constraints:

0 ≤ x ≤ 100"""

#code_Solution

x = int(input())

# code here
while x>= 0:
    print(x,end=' ')
    x -= 1
