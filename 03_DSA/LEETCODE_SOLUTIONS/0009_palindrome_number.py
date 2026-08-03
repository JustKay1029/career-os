# LeetCode 9. Palindrome Number
# Problem Link: https://leetcode.com/problems/palindrome-number/
#
# Time Complexity: O(log10(N)) / O(D) where D is the number of digits in the integer x.
# Space Complexity: O(D) to store the string representation.
#
# Key Realization & Learnings:
# 1. Python-specific approach: 
#    - Convert the integer to a string `s = str(x)`.
#    - Compare it with its reverse using slicing `s == s[::-1]`.
# 2. General Mathematical Approach (Non-string conversion):
#    - Negative numbers are not palindromes (due to the '-' sign).
#    - Numbers ending with 0 (except 0 itself) are not palindromes.
#    - Revert the second half of the number mathematically:
#      ```python
#      if x < 0 or (x % 10 == 0 and x != 0):
#          return False
#      reverted_number = 0
#      while x > reverted_number:
#          reverted_number = reverted_number * 10 + x % 10
#          x //= 10
#      return x == reverted_number or x == reverted_number // 10
#      ```

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
