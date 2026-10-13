"""Given a string s, find if it is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Constraints:

1 ≤ s.size() ≤ 106
s consists only of lowercase English alphabets"""

class Solution:
    def isPalindrome(self, s):
        # code here
        left = 0
        right = len(s) - 1
        
        while left<right:
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
