# LeetCode 344. Reverse String
# Problem Link: https://leetcode.com/problems/reverse-string/
#
# Time Complexity: O(N) where N is the length of string s. We traverse the string once.
# Space Complexity: O(1) as we modify the input array in-place without allocating extra space.
#
# Key Realization & Learnings:
# 1. Two Pointers Technique: Place one pointer at the start (left) and one at the end (right) of the array.
# 2. In-place swapping: Swap the elements at the pointers and move them towards each other (left += 1, right -= 1) until they meet.
# 3. Python Swapping: Python's parallel assignment `a, b = b, a` allows swapping variables cleanly in a single line without a temporary variable.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
