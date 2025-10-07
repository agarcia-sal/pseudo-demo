class Solution:
    def minOperations(self, initial: str, target: str) -> int:
        dimension_x = len(initial)
        dimension_y = len(target)
        Q = [[0] * (dimension_y + 1) for _ in range(dimension_x + 1)]
        largest_lcs = 0

        idx_x = 1
        while idx_x <= dimension_x:
            idx_y = 1
            while idx_y <= dimension_y:
                char_in_a = initial[idx_x - 1]
                char_in_b = target[idx_y - 1]
                if not (char_in_a != char_in_b):  # i.e. char_in_a == char_in_b
                    Q[idx_x][idx_y] = Q[idx_x - 1][idx_y - 1] + 1
                    if largest_lcs < Q[idx_x][idx_y]:
                        largest_lcs = Q[idx_x][idx_y]
                idx_y += 1
            idx_x += 1

        total = (dimension_x + dimension_y) - (largest_lcs + largest_lcs)
        return total