# LeetCode 682. Baseball Game
# Problem Link: https://leetcode.com/problems/baseball-game/
#
# Time Complexity: O(N) where N is the number of operations. We process each operation once.
# Space Complexity: O(N) auxiliary stack space to store records.
#
# Key Realization & Learnings:
# 1. Stack Push/Pop Operations:
#    - Utilize a standard stack (list) to maintain active scores.
#    - Operations mapping:
#      - "+": Sum of the last two active scores -> `stack.append(stack[-1] + stack[-2])`.
#      - "D": Double the last active score -> `stack.append(2 * stack[-1])`.
#      - "C": Invalidate/pop the last active score -> `stack.pop()`.
#      - Integer string: Parse and append to the stack -> `stack.append(int(op))`.
# 2. Final Aggregation:
#    - Summing the final elements in the stack yields the correct total score: `return sum(stack)`.

from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)
