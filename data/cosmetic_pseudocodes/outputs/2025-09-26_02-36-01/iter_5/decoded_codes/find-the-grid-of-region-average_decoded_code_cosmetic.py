from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        accum = [[0] * width for _ in range(height)]
        freq = [[0] * width for _ in range(height)]

        def check_region_validity(a: int, b: int) -> bool:
            def recur_i(i_current: int) -> bool:
                if i_current == a + 3:
                    return True

                def recur_j(j_current: int) -> bool:
                    if j_current == b + 3:
                        return recur_i(i_current + 1)

                    neighbor_offsets = [(-1,0), (1,0), (0,-1), (0,1)]

                    def check_neighbor(k: int) -> bool:
                        if k == len(neighbor_offsets):
                            return recur_j(j_current + 1)

                        dx, dy = neighbor_offsets[k]
                        ni = i_current + dx
                        nj = j_current + dy

                        if 0 <= ni < a + 3 and 0 <= nj < b + 3:
                            diff = image[i_current][j_current] - image[ni][nj]
                            # Check if difference magnitude exceeds threshold
                            if (diff < 0 and -diff > threshold) or (diff > 0 and diff > threshold):
                                return False
                        return check_neighbor(k + 1)
                    return check_neighbor(0)
                return recur_j(b)
            return recur_i(a)

        def compute_avg(p: int, q: int) -> int:
            def sum_i(idx_i: int, total_sum: int) -> int:
                if idx_i == p + 3:
                    return total_sum

                def sum_j(idx_j: int, acc: int) -> int:
                    if idx_j == q + 3:
                        return sum_i(idx_i + 1, acc)
                    updated_acc = acc + image[idx_i][idx_j]
                    return sum_j(idx_j + 1, updated_acc)
                return sum_j(q, total_sum)
            total_sum = sum_i(p, 0)
            divisor = 9
            return total_sum // divisor

        def outer_loop_i(ii: int) -> None:
            if ii > height - 3:
                return

            def outer_loop_j(jj: int) -> None:
                if jj > width - 3:
                    return

                valid_region_flag = check_region_validity(ii, jj)
                if valid_region_flag:
                    avg_val = compute_avg(ii, jj)

                    def update_region(u: int) -> None:
                        if u == ii + 3:
                            return

                        def update_col(v: int) -> None:
                            if v == jj + 3:
                                return
                            accum[u][v] += avg_val
                            freq[u][v] += 1
                            update_col(v + 1)
                        update_col(jj)
                        update_region(u + 1)
                    update_region(ii)
                outer_loop_j(jj + 1)
            outer_loop_j(0)
            outer_loop_i(ii + 1)
        outer_loop_i(0)

        def finalize_rows(r: int) -> None:
            if r == height:
                return

            def finalize_cols(c: int) -> None:
                if c == width:
                    return
                if freq[r][c] > 0:
                    accum[r][c] = accum[r][c] // freq[r][c]
                else:
                    accum[r][c] = image[r][c]
                finalize_cols(c + 1)
            finalize_cols(0)
            finalize_rows(r + 1)
        finalize_rows(0)

        return accum