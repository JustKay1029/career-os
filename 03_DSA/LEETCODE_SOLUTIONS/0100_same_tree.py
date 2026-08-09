# LeetCode 100. Same Tree
# Problem Link: https://leetcode.com/problems/same-tree/
#
# Time Complexity: O(min(N, M)) where N and M are the number of nodes in trees p and q respectively. 
#                  We traverse both trees concurrently and stop as soon as a mismatch is found.
# Space Complexity: O(min(H1, H2)) where H1 and H2 are the heights of trees p and q respectively, 
#                  representing recursion stack frames.
#
# Key Realization & Learnings:
# 1. Structural and Value Equality Check:
#    - Base Case 1: If both nodes are `None`, the subtrees are structurally identical (empty). Return `True`.
#    - Base Case 2: If only one of the nodes is `None`, there is a structural mismatch. Return `False`.
#    - Base Case 3: If both nodes exist but their values differ, return `False`.
# 2. Divide and Conquer Recursion:
#    - The trees are identical if the current nodes are equal AND their left subtrees are identical AND their right subtrees are identical.
#    - Recursive call: `self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)`.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True 
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
