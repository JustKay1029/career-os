# LeetCode 125. Valid Palindrome
# Problem Link: https://leetcode.com/problems/valid-palindrome/
#
# Time Complexity: O(N) where N is the length of string s. We traverse the string at most once.
# Space Complexity: O(1) as we modify pointers in-place without creating a new filtered string.
#
# Key Realization & Learnings:
# 1. Two-Pointer Approach:
#    - Maintain a left pointer `l = 0` and a right pointer `r = len(s) - 1`.
#    - Skip non-alphanumeric characters by checking `not s[l].isalnum()` and `not s[r].isalnum()`.
# 2. Lowercase Comparison:
#    - Compare lowercase characters `s[l] == s[r]`. If not equal, return `False` immediately.
#    - Advance pointers (`l += 1`, `r -= 1`) and repeat until they cross.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer if not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # Move right pointer if not alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare characters
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
