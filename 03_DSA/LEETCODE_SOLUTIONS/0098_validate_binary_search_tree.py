# LeetCode 98. Validate Binary Search Tree
# Problem Link: https://leetcode.com/problems/validate-binary-search-tree/
#
# Time Complexity: O(N) where N is the number of nodes in the binary tree. Each node is visited once.
# Space Complexity: O(H) where H is the height of the tree, representing call stack frames (worst-case O(N)).
#
# Key Realization & Learnings:
# 1. Strict BST Definition:
#    - It is not enough that `root.left.val < root.val` and `root.right.val > root.val`.
#    - ALL nodes in the left subtree must be strictly less than `root.val`, and ALL nodes in the right subtree must be strictly greater than `root.val`.
# 2. Bounded Recursive DFS:
#    - Propagate valid value boundaries `(left_bound, right_bound)` down the tree starting with `(-inf, inf)`.
#    - For any node, check `left_bound < node.val < right_bound`. If violated, return `False`.
#    - When recursing into the left child: upper bound updates to `node.val` -> `(left_bound, node.val)`.
#    - When recursing into the right child: lower bound updates to `node.val` -> `(node.val, right_bound)`.

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float("-inf"), float("inf"))
