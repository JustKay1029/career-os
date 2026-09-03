# LeetCode 567. Permutation in String
# Problem Link: https://leetcode.com/problems/permutation-in-string/
#
# Time Complexity: O(len(s1) + len(s2)) = O(N) where N is the length of s2.
# Space Complexity: O(1) auxiliary space (fixed-size 26-element frequency arrays for lowercase English letters).
#
# Key Realization & Learnings:
# 1. Sliding Window with Character Frequency:
#    - A permutation of `s1` in `s2` means there must exist a substring in `s2` of length `len(s1)` with the exact same character frequencies as `s1`.
#    - If `len(s1) > len(s2)`, no such substring can exist; return `False`.
# 2. Optimized Match Tracking:
#    - Count character frequencies of `s1` and the first `len(s1)` characters of `s2`.
#    - Maintain a `matches` counter indicating how many character counts (out of 26) currently match.
#    - Slide the window of size `len(s1)` across `s2` one character at a time:
#      - Add the incoming character on the right (`r`), updating frequencies and matches.
#      - Remove the outgoing character on the left (`l`), updating frequencies and matches.
#      - If `matches == 26`, a valid permutation window is found; return `True`.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Add right character
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # Remove left character
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1

        return matches == 26
