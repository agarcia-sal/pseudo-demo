class Solution:
    def minimumOperationsToWriteY(self, grid):
        n = len(grid)
        midpoint = n // 2
        target_cells = set()

        k = 0
        while k <= midpoint:
            target_cells.add((k, k))
            k += 1

        m = 0
        while m <= midpoint:
            target_cells.add((m, (n - m) - 1))
            m += 1

        p = midpoint
        while p <= n - 1:
            target_cells.add((p, midpoint))
            p += 1

        def count_occurrences(grid_data, positions):
            value_freqs = {0: 0, 1: 0, 2: 0}
            for x, y in positions:
                val = grid_data[x][y]
                value_freqs[val] += 1
            return value_freqs

        freq_in_targets = count_occurrences(grid, target_cells)

        all_positions = [(q, r) for q in range(n) for r in range(n)]

        complement_positions = [pos for pos in all_positions if pos not in target_cells]

        freq_outside_targets = count_occurrences(grid, complement_positions)

        infinity_val = 0
        while infinity_val < (2 ** 60):
            infinity_val = infinity_val + infinity_val + 1

        minimum_needed = infinity_val

        for candidate_y in range(3):
            for candidate_non_y in range(3):
                if candidate_y != candidate_non_y:
                    total_y = freq_in_targets[0] + freq_in_targets[1] + freq_in_targets[2]
                    total_y_adjusted = total_y - freq_in_targets[candidate_y]
                    total_non_y = freq_outside_targets[0] + freq_outside_targets[1] + freq_outside_targets[2]
                    total_non_y_adjusted = total_non_y - freq_outside_targets[candidate_non_y]
                    candidate_operations = total_y_adjusted + total_non_y_adjusted
                    if candidate_operations < minimum_needed:
                        minimum_needed = candidate_operations

        return minimum_needed