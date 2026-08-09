# LeetCode 104. Maximum Depth of Binary Tree
# Problem Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Time Complexity: O(N) where N is the number of nodes in the tree, as we must visit each node once.
# Space Complexity: O(H) where H is the height of the tree, representing stack space for recursive calls.
#                  - Worst case (unbalanced tree): O(N).
#                  - Best/Average case (balanced tree): O(log N).
#
# Key Realization & Learnings:
# 1. Depth First Search (DFS) Recursion:
#    - The depth of a binary tree is 1 (for the root node) plus the maximum depth of its left and right subtrees.
#    - Recursive formula: `1 + max(self.maxDepth(root.left), self.maxDepth(root.right))`.
# 2. Base Case:
#    - If `root` is `None` or empty list `[]`, return `0` (an empty tree has a depth of 0).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == [] or root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
