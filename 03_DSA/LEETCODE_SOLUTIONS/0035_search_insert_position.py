# LeetCode 35. Search Insert Position
# Problem Link: https://leetcode.com/problems/search-insert-position/
#
# Time Complexity: O(log N) where N is the length of nums, as we halve the search space at each iteration.
# Space Complexity: O(1) constant auxiliary space.
#
# Key Realization & Learnings:
# 1. Custom Binary Search Midpoint:
#    - You implemented the midpoint as `m = (l + r - 1) // 2`.
#    - When searching left/right, if `nums[m] >= target`, we narrow our right bound `r = m`.
#    - If `nums[m] < target`, we narrow our left bound `l = m + 1`.
#    - The final convergence point `l` yields the target index if found, or the insertion point if target does not exist.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = ((l + r - 1) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l
