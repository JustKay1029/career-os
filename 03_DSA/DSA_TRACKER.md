# DSA Tracker

> Tracking problem-solving competence by algorithmic pattern. Aim for structural understanding, not memorization.

---

## 📊 Summary by Pattern

* **Starting Baseline (Pre-Career OS):** 39 Problems Solved (NeetCode Practice)

| Pattern | Solved (New) | Target | Status |
| :--- | :---: | :---: | :--- |
| **Arrays & Hashing** | 4 | 25 | 🟨 In Progress |
| **Two Pointers** | 8 | 20 | 🟨 In Progress |
| **Sliding Window** | 1 | 15 | 🟨 In Progress |
| **Stack & Queue** | 3 | 15 | 🟨 In Progress |
| **Binary Search** | 5 | 15 | 🟨 In Progress |
| **Linked List** | 3 | 15 | 🟨 In Progress |
| **Trees & BST** | 7 | 25 | 🟨 In Progress |
| **Graphs & BFS/DFS** | 0 | 25 | 🟥 Not Started |
| **Dynamic Programming** | 0 | 25 | 🟥 Not Started |

---

## 📝 Log of Solved Problems

Add new entries here as they are solved. Store code files inside the `LEETCODE_SOLUTIONS/` directory.

| # | Date | Problem | Pattern | Difficulty | Solution File | Key Takeaway |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2026-07-17 | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Stack & Queue | Medium | [neetcode-submissions](https://github.com/JustKay1029/neetcode-submissions) | Process tokens sequentially; push operands onto stack and apply operators on top two popped elements. |
| 2 | 2026-07-25 | [67. Add Binary](https://leetcode.com/problems/add-binary/) | Bit Manipulation / Math | Easy | [0067_add_binary.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0067_add_binary.py) | Parse binary strings to integers, sum, and format back to binary. |
| 3 | 2026-07-26 | [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Two Pointers | Hard | [0042_trapping_rain_water.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0042_trapping_rain_water.py) | Prefix/Suffix arrays to precompute max boundary heights at each index; min(L, R) - current height defines trapped water (O(N) space). |
| 4 | 2026-07-27 | [344. Reverse String](https://leetcode.com/problems/reverse-string/) | Two Pointers | Easy | [0344_reverse_string.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0344_reverse_string.py) | Use two converging pointers at both ends of the string; swap elements in-place in O(1) space. |
| 5 | 2026-07-28 | [143. Reorder List](https://leetcode.com/problems/reorder-list/) | Linked List | Medium | [0143_reorder_list.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0143_reorder_list.py) | Find middle (slow/fast), reverse second half, weave/merge both halves (Note: Needs re-learning/retry). |
| 6 | 2026-07-29 | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Linked List | Medium | [0019_remove_nth_node_from_end_of_list.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0019_remove_nth_node_from_end_of_list.py) | Two pointers (slow, fast) with offset n. When fast reaches end, slow points to node before target. |
| 7 | 2026-07-30 | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Linked List | Medium | [0002_add_two_numbers.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0002_add_two_numbers.py) | Digit sum traversal using elementary addition logic (val = v1 + v2 + carry) with dummy head representation. |
| 8 | 2026-07-31 | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Stack & Queue | Hard | [0084_largest_rectangle_in_histogram.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0084_largest_rectangle_in_histogram.py) | Monotonic increasing stack to track indices; pop and calculate area when a shorter bar is encountered. Append 0 height to flush the stack. |
| 9 | 2026-08-01 | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Arrays & Hashing | Easy | [0217_contains_duplicate.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0217_contains_duplicate.py) | Comparison of length len(nums) != len(set(nums)) vs. iterative set traversal seen.add(i) in O(N) time/space. |
| 10 | 2026-08-02 | [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Two Pointers | Easy | [0125_valid_palindrome.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0125_valid_palindrome.py) | Two pointer approach comparing lowercase alphanumeric characters after moving pointers past non-alphanumeric. |
| 11 | 2026-08-03 | [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Two Pointers | Easy | [0009_palindrome_number.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0009_palindrome_number.py) | Python-specific string slicing check s == s[::-1] (Note: Mathematical reversal is also possible without converting to string). |
| 12 | 2026-08-04 | [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Binary Search | Medium | [0875_koko_eating_bananas.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0875_koko_eating_bananas.py) | Binary search on eating speed range [1, max(piles)] checking total_hours <= h (Note: Solved under high fatigue/needs re-solve). |
| 13 | 2026-08-05 | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | Medium | [0003_longest_substring_without_repeating_characters.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0003_longest_substring_without_repeating_characters.py) | Dynamic sliding window using set seen to track characters. Shrink window from left until no duplicates are present. |
| 14 | 2026-08-06 | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Trees & BST | Easy | [0226_invert_binary_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0226_invert_binary_tree.py) | Recursive pre-order traversal swapping left and right child nodes at each level. |
| 15 | 2026-08-07 | [853. Car Fleet](https://leetcode.com/problems/car-fleet/) | Stack & Queue | Medium | [0853_car_fleet.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0853_car_fleet.py) | Sort cars by starting position descending. Calculate arrival times. Use stack to identify slower lead cars that form fleets. |
| 16 | 2026-08-08 | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Trees & BST | Easy | [0104_maximum_depth_of_binary_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0104_maximum_depth_of_binary_tree.py) | Simple recursion: max depth of left and right subtrees + 1. |
| 17 | 2026-08-09 | [100. Same Tree](https://leetcode.com/problems/same-tree/) | Trees & BST | Easy | [0100_same_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0100_same_tree.py) | Recursive structural and value equality check on both subtrees. |
| 18 | 2026-08-10 | [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Arrays & Hashing | Easy | [0014_longest_common_prefix.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0014_longest_common_prefix.py) | Dynamic prefix reduction using startswith checks across strings. |
| 19 | 2026-08-13 | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Trees & BST | Easy | [0110_balanced_binary_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0110_balanced_binary_tree.py) | Top-down recursive height checks recursively checking both subtrees balance status. |
| 20 | 2026-08-14 | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Binary Search | Medium | [0153_find_minimum_in_rotated_sorted_array.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0153_find_minimum_in_rotated_sorted_array.py) | Binary search tracking minimums, adjusting search window based on left-sorted versus right-sorted sub-segment locations. |
| 21 | 2026-08-15 | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Trees & BST | Easy | [0572_subtree_of_another_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0572_subtree_of_another_tree.py) | Recursive traversal evaluating structural same-tree checks for each node of the main tree. |
| 22 | 2026-08-17 | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Trees & BST | Easy | [0543_diameter_of_binary_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0543_diameter_of_binary_tree.py) | DFS recursion calculating height of subtrees and updating max diameter nonlocal variable at each node. |
| 23 | 2026-08-18 | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Binary Search | Medium | [0033_search_in_rotated_sorted_array.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0033_search_in_rotated_sorted_array.py) | Python index lookup (O(N)) (Note: Optimal O(log N) binary search uses split range evaluation). |
| 24 | 2026-08-19 | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Trees & BST | Easy | [0235_lowest_common_ancestor_of_a_binary_search_tree.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0235_lowest_common_ancestor_of_a_binary_search_tree.py) | Iterative BST node value comparison. Moves left/right according to size check bounds until a split is encountered. |
| 25 | 2026-08-20 | [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Arrays & Hashing | Easy | [1929_concatenation_of_array.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/1929_concatenation_of_array.py) | Array replication: loops index i up to 2N copying element values offset by N where i >= N. |
| 26 | 2026-08-21 | [27. Remove Element](https://leetcode.com/problems/remove-element/) | Two Pointers | Easy | [0027_remove_element.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0027_remove_element.py) | Two pointers swap-with-end method. Overwrites matches with last unchecked element without incrementing pointer. |
| 27 | 2026-08-23 | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) | Arrays & Hashing | Medium | [0912_sort_an_array.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0912_sort_an_array.py) | Merge sort implementation: divide array in half recursively and merge sorted segments in O(N log N) time. |
| 28 | 2026-08-24 | [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Binary Search | Easy | [0069_sqrtx.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0069_sqrtx.py) | Python-specific float sqrt cast conversion check (Note: Optimal integer math O(log N) binary search reference added). |
| 29 | 2026-08-25 | [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Binary Search | Easy | [0035_search_insert_position.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0035_search_insert_position.py) | Custom binary search interval convergence loop returning left index convergence target position. |
| 30 | 2026-08-26 | [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Two Pointers | Easy | [0680_valid_palindrome_ii.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0680_valid_palindrome_ii.py) | Two pointers greedy palindrome validation branching into skipped left or right checks upon mismatch detection. |
| 31 | 2026-08-27 | [189. Rotate Array](https://leetcode.com/problems/rotate-array/) | Two Pointers | Medium | [0189_rotate_array.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0189_rotate_array.py) | In-place element rotation by shifting elements via insertions/pops (Note: Optimal O(N) 3-step reversal reference added). |
| 32 | 2026-08-29 | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) | Two Pointers | Medium | [0075_sort_colors.py](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/03_DSA/LEETCODE_SOLUTIONS/0075_sort_colors.py) | Two-pass counting sort tracking frequencies of 0, 1, and 2. (Note: Optimal one-pass Dutch National Flag algorithm reference added). |




---

## 🗃️ Folder Structure
Create your solution files in `03_DSA/LEETCODE_SOLUTIONS/` using a standardized naming convention: `XXX_problem_name.py`. Add a comment block at the top with:
1. Problem description link.
2. Time & Space Complexity analysis.
3. Key realizations during implementation.
