# LeetCode 1929. Concatenation of Array
# Problem Link: https://leetcode.com/problems/concatenation-of-array/
#
# Time Complexity: O(N) where N is the size of input array nums, as we must copy the elements to the new doubled array.
# Space Complexity: O(N) auxiliary space (O(2N) to construct the output concatenation array).
#
# Key Realization & Learnings:
# 1. Iterative Construction:
#    - Allocate a result array `ans` of size `2N`.
#    - Loop through index `i` from `0` to `2N - 1`. If `i >= N`, copy from `nums[i - N]`; otherwise copy from `nums[i]`.
# 2. Python Shorthand Shortcut (Alternative):
#    - Python's list multiplication makes this trivial: `return nums * 2` (runs highly optimized in C under the hood).

from typing import List

class Solution:
    # Iterative assignment variation
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n * 2
        for i in range(n * 2):
            if i >= n:
                ans[i] = nums[i - n]
            else:
                ans[i] = nums[i]
        return ans

    # Python shorthand alternative
    def getConcatenation_shorthand(self, nums: List[int]) -> List[int]:
        return nums * 2
