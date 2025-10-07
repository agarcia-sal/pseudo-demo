from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        p = len(image)
        q = len(image[0]) if p > 0 else 0
        arr = [[0] * q for _ in range(p)]
        freq = [[0] * q for _ in range(p)]

        def check_region(a: int, b: int) -> bool:
            for u in range(a, a + 3):
                for v in range(b, b + 3):
                    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for dx, dy in deltas:
                        cur_x, cur_y = u + dx, v + dy
                        if 0 <= cur_x < a + 3 and 0 <= cur_y < b + 3:
                            if abs(image[u][v] - image[cur_x][cur_y]) > threshold:
                                return False
            return True

        def avg_calc(c: int, d: int) -> int:
            sum_val = 0
            for m_idx in range(c, c + 3):
                for n_idx in range(d, d + 3):
                    sum_val += image[m_idx][n_idx]
            return sum_val // 9

        outer_i = 0
        while outer_i <= p - 3:
            outer_j = 0
            while outer_j <= q - 3:
                if check_region(outer_i, outer_j):
                    av = avg_calc(outer_i, outer_j)
                    for inner_x in range(outer_i, outer_i + 3):
                        for inner_y in range(outer_j, outer_j + 3):
                            arr[inner_x][inner_y] += av
                            freq[inner_x][inner_y] += 1
                outer_j += 1
            outer_i += 1

        for idx_i in range(p):
            for idx_j in range(q):
                if freq[idx_i][idx_j] > 0:
                    arr[idx_i][idx_j] //= freq[idx_i][idx_j]
                else:
                    arr[idx_i][idx_j] = image[idx_i][idx_j]

        return arr