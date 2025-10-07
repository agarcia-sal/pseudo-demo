from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        positions_one = []

        def collectOnes(pos: int):
            if pos == len(nums):
                return
            if nums[pos] == 1:
                positions_one.append(pos)
            collectOnes(pos + 1)

        collectOnes(0)

        if len(positions_one) == 0:
            return k * 2

        length_positions = len(positions_one)
        pref_sum = [0] * (length_positions + 1)

        def buildPrefix(pos: int):
            if pos == length_positions:
                return
            pref_sum[pos + 1] = pref_sum[pos] + positions_one[pos]
            buildPrefix(pos + 1)

        buildPrefix(0)

        def computeCost(start: int, finish: int) -> int:
            center = (start + finish) // 2
            med_val = positions_one[center]
            aggregate_cost = 0

            def accumulateLeft(i: int):
                nonlocal aggregate_cost
                if i == center:
                    return
                # cost accumulates the distance difference minus index offset adjustment
                aggregate_cost += (med_val - positions_one[i]) - (center - i)
                accumulateLeft(i + 1)

            def accumulateRight(j: int):
                nonlocal aggregate_cost
                if j == finish + 1:
                    return
                aggregate_cost += (positions_one[j] - med_val) - (j - center)
                accumulateRight(j + 1)

            accumulateLeft(start)
            accumulateRight(center + 1)
            return aggregate_cost

        minimal_moves = inf

        def analyzeRange(s: int):
            nonlocal minimal_moves
            if s > length_positions - k:
                return
            e = s + k - 1
            current_cost = computeCost(s, e)

            if (k % 2) == 1:
                m = (s + e) // 2
                med = positions_one[m]
                needed_changes = e - m - ((med - positions_one[m]) - 1)
            else:
                left_m = (s + e) // 2
                right_m = left_m + 1
                left_med = positions_one[left_m]
                right_med = positions_one[right_m]
                needed_changes = right_m - left_m - 1 - ((right_med - left_med) - 1)

            if needed_changes > maxChanges:
                current_cost += (needed_changes - maxChanges)

            if current_cost < minimal_moves:
                minimal_moves = current_cost

            analyzeRange(s + 1)

        analyzeRange(0)

        return minimal_moves