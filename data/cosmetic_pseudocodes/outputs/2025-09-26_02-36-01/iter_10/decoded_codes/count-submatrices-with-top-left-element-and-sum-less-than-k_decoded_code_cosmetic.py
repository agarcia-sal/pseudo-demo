class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0

        t0 = 0
        t1 = len(grid)
        t2 = len(grid[0])

        prefix_sum = [[0] * t2 for _ in range(t1)]
        count_accumulator = 0

        def rec_ixi(xi):
            if xi >= t1:
                return

            def rec_yj(yj):
                nonlocal count_accumulator
                if yj >= t2:
                    return

                def calc_value():
                    if xi == 0 and yj == 0:
                        return grid[xi][yj]
                    elif xi == 0:
                        return prefix_sum[xi][yj - 1] + grid[xi][yj]
                    elif yj == 0:
                        return prefix_sum[xi - 1][yj] + grid[xi][yj]
                    else:
                        return (prefix_sum[xi - 1][yj]
                                + prefix_sum[xi][yj - 1]
                                - prefix_sum[xi - 1][yj - 1]
                                + grid[xi][yj])

                prefix_sum[xi][yj] = calc_value()
                if prefix_sum[xi][yj] <= k:
                    count_accumulator += 1

                rec_yj(yj + 1)

            rec_yj(0)
            rec_ixi(xi + 1)

        rec_ixi(0)

        return count_accumulator