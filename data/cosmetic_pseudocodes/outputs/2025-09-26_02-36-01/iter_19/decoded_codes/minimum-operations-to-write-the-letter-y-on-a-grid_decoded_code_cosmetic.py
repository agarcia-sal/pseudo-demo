from collections import defaultdict
from math import inf

class Solution:
    def minimumOperationsToWriteY(self, grid):
        delta = len(grid)
        midpoint = delta // 2
        alpha = set()

        j = 0
        while j <= midpoint:
            alpha.add((j, j))
            j += 1

        k = 0
        while True:
            alpha.add((k, delta - k - 1))
            k += 1
            if k > midpoint:
                break

        z = midpoint
        while z <= delta - 1:
            alpha.add((z, midpoint))
            z += 1

        def compute_frequency(coords, matrix):
            freq_map = defaultdict(int)
            for x_val, y_val in coords:
                element = matrix[x_val][y_val]
                freq_map[element] += 1
            return freq_map

        letter_y_counts = compute_frequency(alpha, grid)

        def compute_non_counters(coords, matrix, size):
            freq_map = defaultdict(int)
            for m in range(size):
                for n in range(size):
                    if (m, n) not in coords:
                        val = matrix[m][n]
                        freq_map[val] += 1
            return freq_map

        non_letter_y_counts = compute_non_counters(alpha, grid, delta)

        smallest_ops = inf

        def sum_map_values(m):
            return sum(m.values())

        a = 0
        while a <= 2:
            b = 0
            while b <= 2:
                if a != b:
                    sum_y_values = sum_map_values(letter_y_counts)
                    removals_y = letter_y_counts[a] if a in letter_y_counts else 0
                    sum_non_y_values = sum_map_values(non_letter_y_counts)
                    removals_non_y = non_letter_y_counts[b] if b in non_letter_y_counts else 0
                    candidate = (sum_y_values - removals_y) + (sum_non_y_values - removals_non_y)
                    if candidate < smallest_ops:
                        smallest_ops = candidate
                b += 1
            a += 1

        return smallest_ops