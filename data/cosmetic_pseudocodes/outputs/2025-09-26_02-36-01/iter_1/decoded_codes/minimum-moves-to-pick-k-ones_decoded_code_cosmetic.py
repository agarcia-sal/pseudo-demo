from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        ones_indices = [i for i, val in enumerate(nums) if val == 1]
        if not ones_indices:
            return k * 2

        count_ones = len(ones_indices)
        prefix = [0] * (count_ones + 1)
        for j in range(count_ones):
            prefix[j + 1] = prefix[j] + ones_indices[j]

        def compute_cost(left: int, right: int) -> int:
            mid_pos = (left + right) // 2
            median_val = ones_indices[mid_pos]
            total_cost = 0

            for idx in range(left, mid_pos):
                total_cost += (median_val - ones_indices[idx]) - (mid_pos - idx)
            for idx in range(mid_pos + 1, right + 1):
                total_cost += (ones_indices[idx] - median_val) - (idx - mid_pos)

            return total_cost

        minimum_moves = inf
        for start_pos in range(count_ones - k + 1):
            end_pos = start_pos + k - 1
            moving_cost = compute_cost(start_pos, end_pos)

            if k % 2 == 1:
                mid_pos = (start_pos + end_pos) // 2
                median_value = ones_indices[mid_pos]
                needed_changes = (end_pos - mid_pos) - (median_value - ones_indices[mid_pos] - 1)
            else:
                left_mid = (start_pos + end_pos) // 2
                right_mid = left_mid + 1
                left_median_val = ones_indices[left_mid]
                right_median_val = ones_indices[right_mid]
                needed_changes = (right_mid - left_mid - 1) - (right_median_val - left_median_val - 1)

            if needed_changes > maxChanges:
                moving_cost += (needed_changes - maxChanges)

            if moving_cost < minimum_moves:
                minimum_moves = moving_cost

        return minimum_moves