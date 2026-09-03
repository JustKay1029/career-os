# LeetCode 374. Guess Number Higher or Lower
# Problem Link: https://leetcode.com/problems/guess-number-higher-or-lower/
#
# Time Complexity: O(log N) where N is the upper bound of the number range.
# Space Complexity: O(1) constant auxiliary space.
#
# Key Realization & Learnings:
# 1. Classic Binary Search Search Space [1, n]:
#    - The search space is ordered and monotonic from 1 to n.
#    - Pick the midpoint `mid = (l + r) // 2`.
#    - Query the API `guess(mid)`:
#      - If `guess(mid) == 0`: Midpoint is the target number; return `mid`.
#      - If `guess(mid) == -1`: The picked number is lower than guess; narrow right bound: `r = mid - 1`.
#      - If `guess(mid) == 1`: The picked number is higher than guess; narrow left bound: `l = mid + 1`.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                r = mid - 1
            else:
                l = mid + 1
        return -1
