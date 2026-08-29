# LeetCode 75. Sort Colors
# Problem Link: https://leetcode.com/problems/sort-colors/
#
# Time Complexity: O(N) where N is the length of nums.
#                  - Counting Sort (submitted): Two passes (one to count, one to overwrite).
#                  - Dutch National Flag (optimal): One pass.
# Space Complexity: O(1) in-place modification.
#
# Key Realization & Learnings:
# 1. Counting Sort (Two-pass approach):
#    - Maintain a frequency array `count` of size 3 to count occurrences of 0, 1, and 2.
#    - In the second pass, overwrite `nums` sequentially based on the frequencies.
# 2. Dutch National Flag Algorithm (Optimal One-pass approach):
#    - Maintain three pointers: `low` (boundary of 0s), `mid` (current element), and `high` (boundary of 2s).
#    - Traverse with `mid` from 0 to `high`:
#      a. If `nums[mid] == 0`: swap `nums[low]` and `nums[mid]`, increment `low` and `mid`.
#      b. If `nums[mid] == 1`: just increment `mid`.
#      c. If `nums[mid] == 2`: swap `nums[mid]` and `nums[high]`, decrement `high` (do not increment `mid` yet, as the swapped element from the end is unchecked).

from typing import List

class Solution:
    # Submitted Two-pass Counting Sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[index] = i
                index += 1

    # Optimal One-pass Dutch National Flag algorithm for reference
    def sortColors_optimal(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
