# LeetCode 143. Reorder List
# Problem Link: https://leetcode.com/problems/reorder-list/
#
# Time Complexity: O(N) where N is the number of nodes in the linked list. 
#                  - Finding middle: O(N)
#                  - Reversing second half: O(N)
#                  - Merging halves: O(N)
# Space Complexity: O(1) as we modify the pointers in-place.
#
# Key Realization & Learnings:
# 1. 3-Step Strategy:
#    - Step 1: Find the middle of the list using slow and fast pointers.
#    - Step 2: Reverse the second half of the list starting from slow.next.
#    - Step 3: Merge/weave the first half and the reversed second half together.
# 2. Reflection:
#    - Note: This question is syntactically heavy and requires precise pointer re-routing. Need to review the logic and practice it again to master it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find the middle using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev, curr = None, slow.next
        slow.next = None  # Cut the first half from the second half

        while curr:
            nxt_temp = curr.next
            curr.next = prev
            prev = curr
            curr = nxt_temp

        # Step 3: Merge/weave the two halves together
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
