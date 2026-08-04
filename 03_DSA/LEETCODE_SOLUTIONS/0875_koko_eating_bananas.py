# LeetCode 875. Koko Eating Bananas
# Problem Link: https://leetcode.com/problems/koko-eating-bananas/
#
# Time Complexity: O(N * log(max(P))) where N is the number of piles and P is the sizes of piles.
#                  - We perform binary search over the range [1, max(piles)], taking log(max(P)) steps.
#                  - At each step, we iterate through piles to compute total hours (takes O(N) time).
# Space Complexity: O(1) as we use constant extra space.
#
# Key Realization & Learnings:
# 1. Binary Search on Search Space:
#    - Instead of binary searching on the input array, binary search on the *answer* range (eating speeds `k`).
#    - The minimum speed is `1` banana/hour, and the maximum is `max(piles)` bananas/hour.
# 2. Feasibility Condition:
#    - For each midpoint speed `k`, compute total hours `sum(ceil(pile / k))`.
#    - If `total_hours <= h`, it's feasible: record the answer and search for a smaller speed in the left half (`hi = k - 1`).
#    - Otherwise, Koko eats too slowly: search for a larger speed in the right half (`lo = k + 1`).
# 3. Honest Reflection:
#    - Note: Copied today due to high fatigue and low energy, but committed to keeping the daily streak alive. Must re-solve this completely from scratch to internalize binary search on answer spaces.

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)
        lo = 1
        ans = hi
        while lo <= hi:
            k = (hi + lo) // 2
            # Calculate total hours needed at speed k
            total_hours = sum(math.ceil(pile / k) for pile in piles)
            if total_hours <= h:
                ans = k
                hi = k - 1
            else:
                lo = k + 1
        return ans
