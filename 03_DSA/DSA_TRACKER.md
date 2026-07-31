# DSA Tracker

> Tracking problem-solving competence by algorithmic pattern. Aim for structural understanding, not memorization.

---

## 📊 Summary by Pattern

* **Starting Baseline (Pre-Career OS):** 39 Problems Solved (NeetCode Practice)

| Pattern | Solved (New) | Target | Status |
| :--- | :---: | :---: | :--- |
| **Arrays & Hashing** | 0 | 25 | 🟧 Restarting |
| **Two Pointers** | 2 | 20 | 🟨 In Progress |
| **Sliding Window** | 0 | 15 | 🟥 Not Started |
| **Stack & Queue** | 2 | 15 | 🟨 In Progress |
| **Binary Search** | 0 | 15 | 🟥 Not Started |
| **Linked List** | 3 | 15 | 🟨 In Progress |
| **Trees & BST** | 0 | 25 | 🟥 Not Started |
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



---

## 🗃️ Folder Structure
Create your solution files in `03_DSA/LEETCODE_SOLUTIONS/` using a standardized naming convention: `XXX_problem_name.py`. Add a comment block at the top with:
1. Problem description link.
2. Time & Space Complexity analysis.
3. Key realizations during implementation.
