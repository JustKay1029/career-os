# LeetCode 27. Remove Element
# Problem Link: https://leetcode.com/problems/remove-element/
#
# Time Complexity: O(N) where N is the length of nums. In the worst case, we scan the array once.
# Space Complexity: O(1) as we modify the array in-place.
#
# Key Realization & Learnings:
# 1. Swapping with the End Elements (Why nums[i] = nums[n] works):
#    - Since the order of elements can be changed, instead of shifting all elements to the left (which takes O(N) time per element deletion), we swap the target element at index `i` with the last element of the valid search array.
#    - Specifically: when `nums[i] == val`, we decrement our valid array bounds `n` by 1: `n -= 1`. Then we overwrite the match at index `i` with the value at the newly decremented end index: `nums[i] = nums[n]`.
#    - This effectively discards the matched element at the end and brings an unchecked element to index `i` to be processed.
# 2. Pointer Controls (Why we do NOT increment `i` in the if clause):
#    - The newly copied element `nums[n]` at index `i` has NOT been inspected yet. It could also be equal to `val`.
#    - If we incremented `i` immediately (`i += 1`), we would skip checking this newly moved element, potentially leaving a target `val` inside our final filtered subarray boundary.
#    - By keeping `i` unchanged when a replacement occurs, the loop evaluates the new element at `nums[i]` on the next iteration. Only when `nums[i] != val` do we safely increment: `else: i += 1`.
# 3. Pythonic Alternative:
#    - We can use built-in array mutations: `while val in nums: nums.remove(val)`. Under the hood, this repeated `.remove()` scans the list and shifts elements, leading to O(N^2) worst-case time complexity, whereas the swap-with-end pointer approach is strictly O(N).

from typing import List

class Solution:
    # Two-pointers swap-with-end (Optimal O(N) time / O(1) space)
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1 
                nums[i] = nums[n]  # Overwrite match with last unchecked element
            else:
                i += 1             # Only increment pointer when element is valid/inspected
        return n

    # Pythonic built-in way (O(N^2) time complexity)
    def removeElement_pythonic(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
