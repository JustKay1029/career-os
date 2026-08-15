# LeetCode 572. Subtree of Another Tree
# Problem Link: https://leetcode.com/problems/subtree-of-another-tree/
#
# Time Complexity: O(N * M) where N is the number of nodes in root tree, and M is the number of nodes in subRoot tree.
#                  In the worst case, we run isSameTree on every node of root.
# Space Complexity: O(H) where H is the height of root tree, representing recursion stack space.
#
# Key Realization & Learnings:
# 1. Structural Comparison:
#    - A tree `subRoot` is a subtree of `root` if:
#      a. The trees are identical (using `isSameTree` match check).
#      b. Or `subRoot` is a subtree of the left child of `root`.
#      c. Or `subRoot` is a subtree of the right child of `root`.
# 2. Base Cases:
#    - An empty tree `subRoot` is always a subtree of any tree (returns `True`).
#    - If `root` is empty but `subRoot` is not, `subRoot` cannot be a subtree (returns `False`).
# 3. Helper isSameTree:
#    - Recursively checks value equivalence and structural alignment concurrently.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
