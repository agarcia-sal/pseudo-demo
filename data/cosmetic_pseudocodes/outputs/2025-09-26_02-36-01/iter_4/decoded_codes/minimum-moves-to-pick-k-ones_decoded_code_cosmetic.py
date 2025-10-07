class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        positions_of_ones = []
        idx = 0
        length = len(nums)
        while idx < length:
            if nums[idx] == 1:
                positions_of_ones.append(idx)
            idx += 1

        if len(positions_of_ones) == 0:
            return k * 2

        count_ones = len(positions_of_ones)
        accum_sums = [0] * (count_ones + 1)
        i = 0
        while i < count_ones:
            accum_sums[i + 1] = accum_sums[i] + positions_of_ones[i]
            i += 1

        def cost(start: int, end: int) -> int:
            midpoint = (start + end) // 2
            median_val = positions_of_ones[midpoint]
            total_cost = 0

            j = start
            while j < midpoint:
                val1 = (median_val - positions_of_ones[j]) - (midpoint - j)
                total_cost += val1
                j += 1

            j = midpoint + 1
            while j <= end:
                val2 = (positions_of_ones[j] - median_val) - (j - midpoint)
                total_cost += val2
                j += 1

            return total_cost

        minimal_moves = float('inf')

        s = 0
        while s <= count_ones - k:
            e = s + k - 1
            cur_cost = cost(s, e)

            if (k % 2) != 0:
                mid_idx = (s + e) // 2
                med_val = positions_of_ones[mid_idx]
                needed_changes = (e - mid_idx) - (med_val - positions_of_ones[mid_idx] - 1)
            else:
                left_mid = (s + e) // 2
                right_mid = left_mid + 1
                left_med = positions_of_ones[left_mid]
                right_med = positions_of_ones[right_mid]
                needed_changes = (right_mid - left_mid - 1) - (right_med - left_med - 1)

            if needed_changes > maxChanges:
                cur_cost += needed_changes - maxChanges

            if cur_cost < minimal_moves:
                minimal_moves = cur_cost

            s += 1

        return minimal_moves