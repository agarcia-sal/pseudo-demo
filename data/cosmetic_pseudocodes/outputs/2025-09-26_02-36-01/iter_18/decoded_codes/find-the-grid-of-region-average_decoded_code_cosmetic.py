from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        alpha = len(image)
        beta = len(image[0]) if image else 0
        omega = [[0] * beta for _ in range(alpha)]
        zeta = [[0] * beta for _ in range(alpha)]

        def is_valid_region(p: int, q: int) -> bool:
            for idx in range(p, p + 3):
                for jdx in range(q, q + 3):
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx_ = idx + dx
                        ny_ = jdx + dy
                        if not (p <= nx_ < p + 3 and q <= ny_ < q + 3):
                            continue
                        if abs(image[idx][jdx] - image[nx_][ny_]) > threshold:
                            return False
            return True

        def calculate_average(a: int, b: int) -> int:
            summation = 0
            for cnt1 in range(a, a + 3):
                for cnt2 in range(b, b + 3):
                    summation += image[cnt1][cnt2]
            return summation // 9

        outer_i = 0
        while outer_i <= alpha - 3:
            outer_j = 0
            while outer_j <= beta - 3:
                if is_valid_region(outer_i, outer_j):
                    val_avg = calculate_average(outer_i, outer_j)
                    inner_x = outer_i
                    while inner_x < outer_i + 3:
                        inner_y = outer_j
                        while inner_y < outer_j + 3:
                            omega[inner_x][inner_y] += val_avg
                            zeta[inner_x][inner_y] += 1
                            inner_y += 1
                        inner_x += 1
                outer_j += 1
            outer_i += 1

        idx_i = 0
        while idx_i < alpha:
            idx_j = 0
            while idx_j < beta:
                if zeta[idx_i][idx_j] > 0:
                    omega[idx_i][idx_j] //= zeta[idx_i][idx_j]
                else:
                    omega[idx_i][idx_j] = image[idx_i][idx_j]
                idx_j += 1
            idx_i += 1

        return omega