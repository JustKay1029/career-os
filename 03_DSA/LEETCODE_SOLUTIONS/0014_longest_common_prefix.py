# LeetCode 14. Longest Common Prefix
# Problem Link: https://leetcode.com/problems/longest-common-prefix/
#
# Time Complexity: O(S) where S is the sum of all characters in all strings.
#                  In the worst case, we compare the prefix against all strings, reducing it character by character.
# Space Complexity: O(1) as we modify the prefix string in-place/use constant extra space.
#
# Key Realization & Learnings:
# 1. Horizontal Scanning / Prefix Reduction:
#    - Initialize the common `prefix` as the entire first string: `strs[0]`.
#    - Loop through the remaining strings `strs[1:]`.
#    - For each string, check if it starts with the current `prefix`. If not, repeatedly trim the last character of `prefix` using slicing: `prefix = prefix[:-1]`.
#    - If `prefix` becomes empty, we can stop early and return `""`.
# 2. Edge Case:
#    - If the input list `strs` is empty, return `""` immediately.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
