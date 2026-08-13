# LeetCode 110. Balanced Binary Tree
# Problem Link: https://leetcode.com/problems/balanced-binary-tree/
#
# Time Complexity: O(N log N) for a balanced tree, as height is called at each node level, and O(N^2) in the worst case (skewed tree).
#                  - Optimal approach would be O(N) by calculating balance-status and height concurrently bottom-up,
#                    but this top-down recursive check works.
# Space Complexity: O(H) where H is the height of the tree, representing stack space for recursive calls.
#
# Key Realization & Learnings:
# 1. Top-Down Recursive Check:
#    - A binary tree is height-balanced if the left and right subtrees of every node differ in height by at most 1: `abs(height(left) - height(right)) <= 1`.
#    - We check this condition at the root, and then recursively check if both the left and right subtrees are balanced: `self.isBalanced(root.left) and self.isBalanced(root.right)`.
# 2. Base Case:
#    - An empty tree (no root) is balanced by definition. Return `True`.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right)> 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1+ max(self.height(root.left), self.height(root.right))
