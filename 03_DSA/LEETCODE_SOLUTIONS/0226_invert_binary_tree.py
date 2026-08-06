# LeetCode 226. Invert Binary Tree
# Problem Link: https://leetcode.com/problems/invert-binary-tree/
#
# Time Complexity: O(N) where N is the number of nodes in the tree. We visit each node exactly once.
# Space Complexity: O(H) where H is the height of the tree, representing stack space for recursive calls. 
#                  - In the worst case (skewed tree), O(N).
#                  - In the best/average case (balanced tree), O(log(N)).
#
# Key Realization & Learnings:
# 1. Recursive Pre-order Traversal:
#    - Swap the left and right children of the current node first: `root.left, root.right = root.right, root.left`.
#    - Recursively invert the left subtree: `self.invertTree(root.left)`.
#    - Recursively invert the right subtree: `self.invertTree(root.right)`.
# 2. Base Case:
#    - If `root` is `None`, return `None` (empty tree/leaf node child).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root 
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 
