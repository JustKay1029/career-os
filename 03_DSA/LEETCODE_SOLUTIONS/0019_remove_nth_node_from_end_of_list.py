# LeetCode 19. Remove Nth Node From End of List
# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Time Complexity: O(N) where N is the length of the linked list. We traverse the list in a single pass.
# Space Complexity: O(1) as we only use a constant amount of extra pointer memory.
#
# Key Realization & Learnings:
# 1. Two-Pointer (Slow/Fast) Offset: 
#    - Move the `fast` pointer `n` steps forward first.
#    - If `fast` becomes `None` immediately, it means we need to remove the head node (first from the start, or Nth from the end), so we simply return `head.next`.
#    - Otherwise, advance both `slow` and `fast` pointers together until `fast.next` is `None`. At this point, the distance between them is `n`, and `slow` is located exactly before the target node to delete.
# 2. Pointer Deletion:
#    - Set `slow.next = slow.next.next` to unlink the target node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
