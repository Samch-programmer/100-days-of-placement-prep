"""Given a number n, use a switch statement to return "One" if the given number is equal to 1, "Two" if the number is 2 and so on till 9 ("Nine") else return "Unknown"(without quotes). 

Examples:

Input: n = 10
Output: Unknown
Input: n = 1
Output: One
Constraints:

1 ≤ n ≤ 100"""

n=int(input())
def get_number_word(n):
    match n:
        case 1: return "One"
        case 2: return "Two"
        case 3: return "Three"
        case 4: return "Four"
        case 5: return "Five"
        case 6: return "Six"
        case 7: return "Seven"
        case 8: return "Eight"
        case 9: return "Nine"
        case _: return "Unknown" 

# Examples
print(get_number_word(n))
