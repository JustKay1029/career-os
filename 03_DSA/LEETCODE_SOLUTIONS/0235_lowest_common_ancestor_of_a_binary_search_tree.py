# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree
# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#
# Time Complexity: O(H) where H is the height of the BST. In the worst case (skewed BST), O(N); in the best/balanced case, O(log N).
# Space Complexity: O(1) as we solve it iteratively without recursion stack frames.
#
# Key Realization & Learnings:
# 1. BST Ordering Property:
#    - For any node `cur`, the left subtree contains strictly smaller values, and the right subtree contains strictly larger values.
#    - If both nodes `p` and `q` have values strictly larger than `cur.val`, their LCA must lie in the right subtree: `cur = cur.right`.
#    - If both nodes `p` and `q` have values strictly smaller than `cur.val`, their LCA must lie in the left subtree: `cur = cur.left`.
# 2. Split Point / LCA Detection:
#    - If one node is on the left and the other is on the right (or if one of the nodes is the current node itself), `cur` is the split point, making it the Lowest Common Ancestor. We return `cur` immediately.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            # If both target nodes lie in the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both target nodes lie in the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # Split point found (one left, one right or current matches p or q)
            else:
                return cur
