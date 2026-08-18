# LeetCode 543. Diameter of Binary Tree
# Problem Link: https://leetcode.com/problems/diameter-of-binary-tree/
#
# Time Complexity: O(N) where N is the number of nodes in the tree, as we visit each node exactly once.
# Space Complexity: O(H) where H is the height of the tree, representing stack space for recursive calls.
#
# Key Realization & Learnings:
# 1. Depth First Search (DFS) Tree Traversal:
#    - The diameter of a tree is the length of the longest path between any two nodes. This path may or may not pass through the root.
#    - For any node, the longest path passing through it is the sum of the heights of its left and right subtrees: `left_height + right_height`.
# 2. Bottom-up Computation:
#    - Use a helper function `dfs(node)` that returns the height of the subtree rooted at `node`.
#    - At each node, compute `left = dfs(node.left)` and `right = dfs(node.right)`.
#    - Update the global maximum diameter: `res = max(res, left + right)`.
#    - Return the height of the current node to its parent: `1 + max(left, right)`.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
