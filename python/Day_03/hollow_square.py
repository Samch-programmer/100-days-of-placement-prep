"""Given an integer n, print the hollow square pattern of size n using '*' character. 

Examples:

Input: n = 4
Output:
* * * *
*     *
*     *
* * * *
Explanation: It's a hollow square! Each side contains n = 4.
Input: n = 3
Output:
* * * 
*   *
* * *
Explanation: It's a hollow square! Each side contains n = 3."""
class Solution:
    def printHollowSquare(self, n):
        # Handle edge case where n is 1
        if n == 1:
            print("*")
            return

        for i in range(n):
            if i == 0 or i == n - 1:
                # Print n stars separated by a space
                print("* " * (n - 1) + "*")
            else:
                # Print left star, correct number of inner spaces, and right star
                print("*" + " " * (2 * n - 3) + "*")
