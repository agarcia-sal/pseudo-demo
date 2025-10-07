class Solution:
    def minimumOperationsToWriteY(self, grid):
        t0 = len(grid)
        t1 = t0 // 2
        t2 = set()

        def add_diag_indices(p1):
            if p1 > t1:
                return
            t2.add((p1, p1))
            add_diag_indices(p1 + 1)

        add_diag_indices(0)

        def add_anti_diag_indices(p3):
            if p3 > t1:
                return
            t2.add((p3, t0 - p3 - 1))
            add_anti_diag_indices(p3 + 1)

        add_anti_diag_indices(0)

        p4 = t0
        while True:
            if p4 < t1:
                break
            t2.add((p4, t1))
            p4 -= 1

        def count_cells(target_set):
            count_map = {0: 0, 1: 0, 2: 0}

            def traverse_row(r):
                if r >= t0:
                    return

                def traverse_col(c):
                    if c >= t0:
                        return
                    if (r, c) in target_set:
                        v = grid[r][c]
                        count_map[v] += 1
                    traverse_col(c + 1)

                traverse_col(0)
                traverse_row(r + 1)

            traverse_row(0)
            return count_map

        t5 = count_cells(t2)

        full_set = set()
        r1 = 0
        while r1 < t0:
            c1 = 0
            while c1 < t0:
                full_set.add((r1, c1))
                c1 += 1
            r1 += 1

        t6 = full_set - t2
        t7 = count_cells(t6)

        t8 = float('inf')
        for r in range(3):
            s = 0
            while s <= 2:
                if r != s:
                    ITER = [0, 1, 2]

                    t_sum = 0

                    def sum_yc(i):
                        nonlocal t_sum
                        if i >= 3:
                            return
                        t_sum += t5[ITER[i]]
                        sum_yc(i+1)

                    sum_yc(0)
                    sum_y = t_sum - t5[r]

                    t_sum = 0

                    def sum_nc(i):
                        nonlocal t_sum
                        if i >= 3:
                            return
                        t_sum += t7[ITER[i]]
                        sum_nc(i+1)

                    sum_nc(0)
                    sum_n = t_sum - t7[s]

                    op = sum_y + sum_n
                    if op < t8:
                        t8 = op
                s += 1

        return t8