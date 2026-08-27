# LeetCode 680. Valid Palindrome II
# Problem Link: https://leetcode.com/problems/valid-palindrome-ii/
#
# Time Complexity: O(N) where N is the length of string s. We scan the string at most twice.
# Space Complexity: O(1) constant auxiliary space.
#
# Key Realization & Learnings:
# 1. Greedy Two-Pointer Evaluation:
#    - Initialize two pointers `left` at 0 and `right` at the end of the string.
#    - Move pointers inward as long as `s[left] == s[right]`.
# 2. Single Character Deletion Choice:
#    - When a mismatch occurs (`s[left] != s[right]`), we have at most one deletion allowed.
#    - We split into two possible sub-evaluations:
#      a. Skip `s[left]` and verify if the remaining substring `s[left + 1 : right]` is a palindrome.
#      b. Skip `s[right]` and verify if the remaining substring `s[left : right - 1]` is a palindrome.
#    - If either of these evaluations returns `True`, then the entire string can be made a palindrome with one deletion.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left character or the right character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1
            
        return True
