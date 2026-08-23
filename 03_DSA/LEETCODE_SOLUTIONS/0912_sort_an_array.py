# LeetCode 912. Sort an Array
# Problem Link: https://leetcode.com/problems/sort-an-array/
#
# Time Complexity: O(N log N) in all cases (best, average, worst) for Merge Sort.
# Space Complexity: O(N) auxiliary space to merge segments.
#
# Key Realization & Learnings:
# 1. Divide and Conquer:
#    - Split the array into two halves recursively until segments have size <= 1 (base case, already sorted).
#    - Sort the left half and right half independently.
# 2. Merging Sorted Segments:
#    - Maintain two pointers `i` and `j` at the start of each sorted segment.
#    - Compare elements and append the smaller one to the output list.
#    - Extend any remaining elements from the left or right segment.

from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)
            
        def merge(left, right):
            res = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            res.extend(left[i:])
            res.extend(right[j:])
            return res
            
        return mergeSort(nums)
