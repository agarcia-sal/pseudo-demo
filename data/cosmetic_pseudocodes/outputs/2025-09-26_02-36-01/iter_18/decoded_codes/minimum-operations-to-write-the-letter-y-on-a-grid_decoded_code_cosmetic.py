from math import inf
from typing import List, Set, Tuple, Dict

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n // 2
        positions: Set[Tuple[int, int]] = set()

        # Add main diagonal positions (r, r) for r in [0..mid]
        for i in range(mid + 1):
            positions.add((i, i))

        # Add anti-diagonal positions (r, n - r - 1) for r in [0..mid]
        for i in range(mid + 1):
            positions.add((i, n - i - 1))

        # Add vertical middle line positions (r, mid) for r in [mid..n-1]
        for r in range(mid, n):
            positions.add((r, mid))

        def count_values_at_positions(pos_set: Set[Tuple[int, int]]) -> Dict[int, int]:
            counts: Dict[int, int] = {}
            for r, c in pos_set:
                val = grid[r][c]
                counts[val] = counts.get(val, 0) + 1
            return counts

        def count_values_not_in_positions(included: Set[Tuple[int, int]]) -> Dict[int, int]:
            counts: Dict[int, int] = {}
            for r in range(n):
                for c in range(n):
                    pos = (r, c)
                    if pos not in included:
                        val = grid[r][c]
                        counts[val] = counts.get(val, 0) + 1
            return counts

        in_counts = count_values_at_positions(positions)
        out_counts = count_values_not_in_positions(positions)

        min_operations = inf

        # yv9sy and ubqxk correspond to digits 0,1,2
        for yv9sy in range(3):
            for ubqxk in range(3):
                if yv9sy != ubqxk:
                    total_in = sum(in_counts.values())
                    total_out = sum(out_counts.values())

                    in_val_count = in_counts.get(yv9sy, 0)
                    out_val_count = out_counts.get(ubqxk, 0)

                    cost_in = total_in - in_val_count
                    cost_out = total_out - out_val_count

                    total_cost = cost_in + cost_out

                    if total_cost < min_operations:
                        min_operations = total_cost

        return min_operations