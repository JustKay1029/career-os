# LeetCode 42. Trapping Rain Water
# Problem Link: https://leetcode.com/problems/trapping-rain-water/
#
# Time Complexity: O(N) where N is the number of elements in the height array. We traverse the array a few times.
# Space Complexity: O(N) to store the prefix max (maxL) and suffix max (maxR) arrays.
#
# Key Realization & Learnings (Reference: dsa.chaicode.com):
# 1. The amount of water trapped at any index i is determined by: min(max_left_height, max_right_height) - height[i].
# 2. This solution uses prefix/suffix arrays to precompute the maximum heights to the left and right of every index in O(N) space.
# 3. Note: This is the "better" O(N) space approach. The optimal O(1) space two-pointer approach is still left to implement.

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)

        maxL = [0]*n
        maxL[0] = height[0]
        for i in range(1, n):
            maxL[i] = max(maxL[i-1], height[i])

        maxR = [0]*n
        maxR[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxR[i] = max(maxR[i+1], height[i])
            
        total = 0
        for i in range(0, n-1):
            total += max(0, min(maxL[i], maxR[i]) - height[i])
        return total
