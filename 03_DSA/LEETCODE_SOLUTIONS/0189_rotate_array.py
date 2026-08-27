# LeetCode 189. Rotate Array
# Problem Link: https://leetcode.com/problems/rotate-array/
#
# Time Complexity: O(k * N) for the shift-by-insertion method (as submitted).
#                  - Optimal approach is O(N) using 3-step array reversal.
# Space Complexity: O(1) in-place modification.
#
# Key Realization & Learnings:
# 1. Insertion Shift (Submitted approach):
#    - For each rotation step (up to `k` times), insert the last element at index 0 and pop the end element.
#    - Since `list.insert(0, val)` takes O(N) time to shift elements, the overall time complexity is O(k * N), which can lead to Time Limit Exceeded (TLE) on large arrays.
# 2. Optimal Reversal Algorithm (O(N) time / O(1) space):
#    - First, modulo `k` by the size of the array: `k = k % len(nums)` (since rotating an array of size N by N steps leaves it unchanged).
#    - 3-Step Reversal Pattern:
#      a. Reverse the entire array.
#      b. Reverse the first `k` elements: index range [0, k-1].
#      c. Reverse the remaining elements: index range [k, N-1].
#    - Reversing any subsegment can be done in O(N) using two pointers swapping values inward.

from typing import List

class Solution:
    # Submitted Shift-by-insertion method (O(k * N) time / O(1) space)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

    # Optimal Reversal Method (O(N) time / O(1) space)
    def rotate_optimal(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                
        reverse(0, n - 1)  # Step 1: Reverse whole array
        reverse(0, k - 1)  # Step 2: Reverse first k elements
        reverse(k, n - 1)  # Step 3: Reverse remaining n-k elements
