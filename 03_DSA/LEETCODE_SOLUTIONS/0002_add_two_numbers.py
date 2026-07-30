# LeetCode 2. Add Two Numbers
# Problem Link: https://leetcode.com/problems/add-two-numbers/
#
# Time Complexity: O(max(N, M)) where N and M are the lengths of the linked lists l1 and l2. We traverse both lists once.
# Space Complexity: O(max(N, M)) to store the newly created result list.
#
# Key Realization & Learnings:
# 1. Dummy Head & Pointer Traversal: 
#    - Utilize a dummy node to start the output list and maintain a `tail` pointer to append newly computed digits.
# 2. Summing digits with Carry:
#    - While l1, l2, or carry exists, compute the digit sum: `v1 + v2 + carry`.
#    - Track carry with integer division `val // 10` and digit value with modulo `val % 10`.
# 3. Original Pseudocode Design:
#    ```
#    out = node; tail = out; carry = 0
#    while l1 or l2 or carry:
#        sum = (l1.val or 0) + (l2.val or 0) + carry
#        carry = sum/10
#        tail.next = node(sum%10)
#        tail = tail.next
#    return out 
#    ```

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            tail.next = ListNode(val)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
