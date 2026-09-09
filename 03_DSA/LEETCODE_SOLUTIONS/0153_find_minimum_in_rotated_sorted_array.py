# LeetCode 153. Find Minimum in Rotated Sorted Array
# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Time Complexity:
#   - Approach 1 (Two Pointers Linear Shrink): O(N) worst-case time, O(1) space.
#   - Approach 2 (Optimal Binary Search): O(log N) time, O(1) space.
# Space Complexity: O(1) in-place auxiliary space for both approaches.
#
# Revision Note (2026-09-09):
# Re-solved and compared two approaches:
# 1. Two Pointers Linear Shrink (Intuitive / Mental-sanity approach):
#    - Maintain left and right pointers.
#    - If `nums[l] < nums[r]`, the window is sorted; the candidate minimum is `nums[l]`, decrement `r`.
#    - If `nums[l] > nums[r]`, `nums[l]` is part of the larger rotated half; increment `l` past it.
#    - While this runs in O(N) worst-case (stepping one element at a time), it is conceptually direct.
#
# 2. Canonical Binary Search (Optimal O(log N) approach):
#    - Compare `nums[mid]` against the right boundary `nums[r]`:
#      a. If `nums[mid] > nums[r]`:
#         - The inflection/drop point (and therefore the minimum) MUST lie strictly to the right of `mid`.
#         - Update left boundary: `l = mid + 1`.
#      b. If `nums[mid] <= nums[r]`:
#         - The right portion is sorted. The minimum is either at `mid` itself or to the left of `mid`.
#         - Update right boundary: `r = mid` (keep mid as a candidate).
#    - Loop terminates when `l == r`, pointing directly to the minimum element.

from typing import List

class Solution:
    # Approach 1: Two Pointers Linear Shrink (O(N) time / O(1) space)
    def findMin_two_pointers(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        ans = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                r -= 1
                ans = nums[l]
            elif nums[l] > nums[r]:
                l += 1
                ans = nums[r]
        return ans

    # Approach 2: Optimal Boundary Comparison Binary Search (O(log N) time / O(1) space)
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # Minimum must be in the right half
                l = mid + 1
            else:
                # Minimum is in the left half (including mid)
                r = mid
        return nums[l]

    # Approach 3: Previous Pivot Tracking Binary Search (Logged on 2026-08-14)
    def findMin_pivot_tracking(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res
