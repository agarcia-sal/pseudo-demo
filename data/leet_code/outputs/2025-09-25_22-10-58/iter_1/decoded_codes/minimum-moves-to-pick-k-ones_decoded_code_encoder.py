from math import inf

class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        one_positions = [i for i, val in enumerate(nums) if val == 1]

        if not one_positions:
            return 2 * k

        n = len(one_positions)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + one_positions[i]

        def cost(start: int, end: int) -> int:
            mid = (start + end) // 2
            median = one_positions[mid]
            total_cost = 0

            # sum of distances on the left side
            for i in range(start, mid):
                total_cost += median - one_positions[i] - (mid - i)
            # sum of distances on the right side
            for i in range(mid + 1, end + 1):
                total_cost += one_positions[i] - median - (i - mid)

            return total_cost

        min_moves = inf

        for start in range(n - k + 1):
            end = start + k - 1
            total_cost = cost(start, end)

            if k % 2 == 1:
                mid = (start + end) // 2
                median = one_positions[mid]
                # changes needed calculation based on median
                changes_needed = end - mid - (median - one_positions[mid] - 1)
            else:
                left_mid = (start + end) // 2
                right_mid = left_mid + 1
                left_median = one_positions[left_mid]
                right_median = one_positions[right_mid]
                changes_needed = right_mid - left_mid - 1 - (right_median - left_median - 1)

            if changes_needed > maxChanges:
                total_cost += changes_needed - maxChanges

            if total_cost < min_moves:
                min_moves = total_cost

        return min_moves