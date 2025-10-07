class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        hamper1, hamper2 = len(grid), len(grid[0])
        # cache[s][r] = [count_X_submatrices, count_Y_submatrices] for prefix up to (s-1, r-1)
        cache = [[[0, 0] for _ in range(hamper2 + 1)] for _ in range(hamper1 + 1)]

        for k1 in range(1, hamper1 + 1):
            for l2 in range(1, hamper2 + 1):
                cache[k1][l2][0] = cache[k1 - 1][l2][0] + cache[k1][l2 - 1][0] - cache[k1 - 1][l2 - 1][0]
                cache[k1][l2][1] = cache[k1 - 1][l2][1] + cache[k1][l2 - 1][1] - cache[k1 - 1][l2 - 1][1]

                cell = grid[k1 - 1][l2 - 1]
                if cell == 'X':
                    cache[k1][l2][0] += 1
                elif cell == 'Y':
                    cache[k1][l2][1] += 1

        tally = 0
        for p_q in range(1, hamper1 + 1):
            for r_s in range(1, hamper2 + 1):
                localA = cache[p_q][r_s][0]
                localB = cache[p_q][r_s][1]

                if localA > 0 and localA == localB:
                    tally += 1

        return tally