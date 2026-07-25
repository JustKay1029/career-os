# LeetCode 67. Add Binary
# Problem Link: https://leetcode.com/problems/add-binary/
#
# Time Complexity: O(N + M) where N and M are the lengths of strings a and b (due to parsing and binary conversion).
# Space Complexity: O(N + M) to store the integer representations and the resulting binary string.
#
# Key Realization & Learnings:
# 1. Base Conversion: You can set the base while converting to int, e.g., int(x, 2) for binary, int(x, 8) for octal, or int(x, 16) for hexadecimal.
# 2. String Slicing: Rather than using string replacement operations (like "-"), Python supports string slicing: str_val[2:] easily strips prefixes like '0b'.
#
# In Python, we can leverage built-in functions: int(x, 2) parses a binary string to a base-10 integer, 
# and bin(y) converts it back to a binary string prefixed with '0b'. Stripping the first two characters 
# returns the correct binary representation.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        A = int(a, 2)
        B = int(b, 2)
        add = A + B 
        bin_sum = bin(add)
        return str(bin_sum)[2:]
