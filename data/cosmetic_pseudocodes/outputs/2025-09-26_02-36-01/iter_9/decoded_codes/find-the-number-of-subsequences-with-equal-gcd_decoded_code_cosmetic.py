class Solution:
    def subsequencePairCount(self, zeta):
        THRESHOLD = 10**9 + 7

        def gcd(alpha, beta):
            while beta != 0:
                alpha, beta = beta, alpha % beta
            return alpha

        apex = 0
        for val in zeta:
            if val > apex:
                apex = val

        row_count = apex + 1
        col_count = apex + 1

        grid_a = [[0] * col_count for _ in range(row_count)]
        grid_a[0][0] = 1

        def mod_add(p, q):
            return (p + q) % THRESHOLD

        for current_val in zeta:
            grid_b = [[0] * col_count for _ in range(row_count)]

            for p_idx in range(row_count):
                for q_idx in range(col_count):
                    original_val = grid_a[p_idx][q_idx]

                    if original_val == 0:
                        continue

                    grid_b[p_idx][q_idx] = mod_add(grid_b[p_idx][q_idx], original_val)

                    gcd_x = gcd(p_idx, current_val)
                    grid_b[gcd_x][q_idx] = mod_add(grid_b[gcd_x][q_idx], original_val)

                    gcd_y = gcd(q_idx, current_val)
                    grid_b[p_idx][gcd_y] = mod_add(grid_b[p_idx][gcd_y], original_val)

            grid_a = grid_b

        omega = 0
        for v_idx in range(1, apex + 1):
            omega = (omega + grid_a[v_idx][v_idx]) % THRESHOLD

        return omega