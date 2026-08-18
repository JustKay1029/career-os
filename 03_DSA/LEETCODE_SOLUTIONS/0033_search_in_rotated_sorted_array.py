# LeetCode 33. Search in Rotated Sorted Array
# Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
#
# Time Complexity: O(N) using Python's built-in array scan index-lookup (as submitted).
#                  - Optimal approach is O(log N) using modified Binary Search.
# Space Complexity: O(1) as we use constant extra space.
#
# Key Realization & Learnings:
# 1. Linear Scan Approach:
#    - We check if `target` exists in the array: `if target not in nums`.
#    - If it doesn't, return `-1`. Otherwise, use `nums.index(target)` to retrieve the element position.
# 2. Optimal Binary Search on Rotated Sorted Array (for interview preparation):
#    - In a rotated sorted array, one half (either left or right) is always sorted.
#    - Compare `nums[mid]` to `nums[l]`:
#      a. If `nums[mid] >= nums[l]`, the left portion is sorted.
#         - If `target` lies within `nums[l] <= target < nums[mid]`, search left (`r = mid - 1`).
#         - Otherwise, search right (`l = mid + 1`).
#      b. Else, the right portion is sorted.
#         - If `target` lies within `nums[mid] < target <= nums[r]`, search right (`l = mid + 1`).
#         - Otherwise, search left (`r = mid - 1`).

from typing import List

class Solution:
    # Submitted O(N) approach
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums: 
            return -1
        return nums.index(target)

    # Optimal O(log N) approach for reference
    def search_optimal(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # Left portion is sorted
            if nums[mid] >= nums[l]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right portion is sorted
            else:
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
