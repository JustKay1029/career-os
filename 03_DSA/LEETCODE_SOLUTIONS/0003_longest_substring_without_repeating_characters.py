# LeetCode 3. Longest Substring Without Repeating Characters
# Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Time Complexity: O(N) where N is the length of string s. Each character is visited at most twice (once by left pointer, once by right pointer).
# Space Complexity: O(min(N, M)) where M is the size of the alphabet/character set.
#
# Key Realization & Learnings:
# 1. Sliding Window Technique:
#    - Maintain a window `[l, r]` of unique characters using a `seen` set.
#    - Expand the window by moving the right pointer `r`.
# 2. Window Shrinking (Duplicate Check):
#    - If `s[r]` already exists in `seen`, shrink the window from the left by removing `s[l]` and incrementing `l` until `s[r]` is no longer in the set.
# 3. Maximum Length:
#    - Update `max_len = max(max_len, r - l + 1)` at each step after ensuring all elements inside the window are unique.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        seen = set()
        max_len = 0
        for r in range(len(s)):
            # While s[r] is a duplicate in our window, shrink from the left
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            # Now that the duplicate is gone, add the new character
            seen.add(s[r])
            # Calculate current window length and update max
            max_len = max(max_len, r - l + 1)
        return max_len
