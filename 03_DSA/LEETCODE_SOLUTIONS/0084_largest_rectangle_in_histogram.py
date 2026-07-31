# LeetCode 84. Largest Rectangle in Histogram
# Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
#
# Time Complexity: O(N) where N is the length of heights. Each index is pushed and popped from the stack at most once.
# Space Complexity: O(N) to store elements in the stack.
#
# Key Realization & Learnings:
# 1. Monotonic Stack: Keep a stack of indices tracking bars of monotonically increasing heights.
# 2. Area Calculation:
#    - When encountering a bar shorter than the bar at the top of the stack, pop from the stack and compute the area.
#    - The popped bar is the height `h`.
#    - The width `w` is the distance between the current index `i` and the index now at the top of the stack (or `i` if the stack is empty).
# 3. Sentinel Value: Append a `0` to the end of the `heights` list to ensure all remaining elements in the stack are popped and processed at the end of the iteration.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                popped_index = stack.pop()
                h = heights[popped_index]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)
        return max_area
