# LeetCode 853. Car Fleet
# Problem Link: https://leetcode.com/problems/car-fleet/
#
# Time Complexity: O(N log N) where N is the number of cars. Sorting the starting positions takes O(N log N), followed by a linear O(N) pass to compute fleets.
# Space Complexity: O(N) to store sorted pairs, times, and stack elements.
#
# Key Realization & Learnings:
# 1. Position Sorting:
#    - Cars cannot pass each other. Therefore, we sort the cars by starting position in descending order (closest to target first).
# 2. Arrival Time Calculation:
#    - For each car, calculate the time to reach the target: `(target - position[i]) / speed[i]`.
# 3. Stack Fleet Tracking:
#    - Iterate through the arrival times (sorted by descending position).
#    - If a car behind arrives *faster* (i.e., its arrival time is `<= stack[-1]`), it will collide with the slower lead car and join its fleet. We skip/continue.
#    - If a car arrives *slower* (i.e., `time > stack[-1]`), it forms a new lead fleet, so we push it onto the stack.
#    - The length of the stack is the final number of car fleets.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed), reverse=True)
        position, speed = map(list, zip(*sorted_pairs))
        times = [0]*(len(position))
        stack = []
        for i in range(len(position)):
            times[i] = (target - position[i]) / speed[i]
        for time in times:
            if stack != [] and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)
