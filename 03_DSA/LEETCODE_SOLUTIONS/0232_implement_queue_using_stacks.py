# LeetCode 232. Implement Queue using Stacks
# Problem Link: https://leetcode.com/problems/implement-queue-using-stacks/
#
# Time Complexity:
#   - Submitted Approach (Python list with pop(0)):
#       push: O(1), pop: O(N) due to shifting elements, peek: O(1), empty: O(1).
#   - Optimal Two-Stack Design:
#       push: O(1), pop: Amortized O(1), worst-case O(N), peek: Amortized O(1), empty: O(1).
# Space Complexity: O(N) to store elements.
#
# Key Realization & Learnings:
# 1. User Submitted Approach:
#    - Implemented a queue wrapper around a single list using `append(x)` and `pop(0)`.
#    - While functional in Python, `pop(0)` takes O(N) time because all subsequent elements must be shifted in memory.
# 2. Optimal Two-Stack Pattern (for interview preparation):
#    - Maintain two stacks: `in_stack` (for pushes) and `out_stack` (for pops/peeks).
#    - On `push(x)`: Append to `in_stack` in O(1).
#    - On `pop()` / `peek()`: If `out_stack` is empty, pop all elements from `in_stack` and push them onto `out_stack` (reversing the order so FIFO is achieved). Then pop/peek from `out_stack`.
#    - Each element is pushed and popped at most twice across the two stacks, yielding an amortized O(1) time per operation.

class MyQueue:
    # Submitted single-list implementation
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not bool(self.queue)


# Optimal Two-Stack Implementation for reference:
class MyQueueTwoStacks:
    def __init__(self):
        self.s1 = []  # Inbound stack
        self.s2 = []  # Outbound stack

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
