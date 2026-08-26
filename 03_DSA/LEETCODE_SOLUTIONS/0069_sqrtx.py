# LeetCode 69. Sqrt(x)
# Problem Link: https://leetcode.com/problems/sqrtx/
#
# Time Complexity: O(1) for math.sqrt (as submitted).
#                  - Optimal binary search approach is O(log x).
# Space Complexity: O(1) constant auxiliary space.
#
# Key Realization & Learnings:
# 1. Float Approximation (Built-in shortcut):
#    - Python's standard `math.sqrt(x)` returns a float value, which we cast to an integer: `int(sqrt(x))`.
#    - Although fast under the hood, it does not demonstrate integer binary search logic.
# 2. Optimal Binary Search (Integer division approach for reference):
#    - Since sqrt(x) lies within the range [0, x], we can run binary search on this interval.
#    - For any midpoint `m`, if `m * m <= x`, it is a potential candidate. We search the right half: `l = m + 1`.
#    - If `m * m > x`, the value is too large. We search the left half: `r = m - 1`.

from math import sqrt

class Solution:
    # Submitted Float Approximation shorthand
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))

    # Optimal O(log x) Binary Search alternative for reference
    def mySqrt_optimal(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x // 2
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
