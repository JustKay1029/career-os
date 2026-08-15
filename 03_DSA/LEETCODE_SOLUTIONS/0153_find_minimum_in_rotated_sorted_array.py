# LeetCode 153. Find Minimum in Rotated Sorted Array
# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Time Complexity: O(log N) where N is the size of the array, since we halve the search space at each iteration.
# Space Complexity: O(1) as we use constant extra space.
#
# Key Realization & Learnings:
# 1. Rotated Sorted Array Properties:
#    - A sorted array rotated at some pivot consists of two sorted sub-segments: `[left_sorted]` and `[right_sorted]`.
#    - If `nums[l] < nums[r]`, the current search window `[l, r]` is already sorted. The minimum is simply `nums[l]`.
# 2. Binary Search Condition:
#    - At midpoint `mid`, if `nums[mid] >= nums[l]`, the pivot lies to the right (left portion is sorted). Move search window right: `l = mid + 1`.
#    - Otherwise, the pivot lies to the left (right portion is sorted, and `mid` is in the right portion). Move search window left: `r = mid - 1`.
#    - We track `res = min(res, nums[mid])` at each iteration to ensure we don't miss the minimum.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            # If the current sub-segment is already sorted, the leftmost element is the minimum of this segment
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # If mid is part of the left sorted portion, pivot is in the right portion
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                # mid is part of the right sorted portion, pivot is to the left
                r = mid - 1
                
        return res
