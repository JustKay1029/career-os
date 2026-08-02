# LeetCode 217. Contains Duplicate / NeetCode Duplicate Integer
# Problem Link: https://leetcode.com/problems/contains-duplicate/
#
# Time Complexity: O(N) where N is the length of nums. Set operations (lookup and insertion) are O(1) on average.
# Space Complexity: O(N) to store elements in the set.
#
# Key Realization & Learnings:
# 1. Approach 1 (Python Inbuilt): `len(nums) != len(set(nums))`
#    - Elegant, clean, and highly optimized in CPython.
#    - Creates a set of the entire list and compares length.
# 2. Approach 2 (Iterative Set Traversal):
#    - More memory efficient if duplicates are found early in a large list, since it returns early without constructing the entire set.
#    - Uses a `seen` set to store visited elements and check existence dynamically.

# Iterative Set Traversal (Early Return)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i) 
        return False

# Inbuilt Python Set Method (Set length comparison)
class SolutionInbuilt:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
