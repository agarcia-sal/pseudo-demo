from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        def region_check(a: int, b: int) -> bool:
            delta_pairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for p in range(a, a + 3):
                for q in range(b, b + 3):
                    for offset_x, offset_y in delta_pairs:
                        nx, ny = p + offset_x, q + offset_y
                        if 0 <= nx < a + 3 and 0 <= ny < b + 3:
                            if abs(image[p][q] - image[nx][ny]) > threshold:
                                return False
            return True

        def avg_calc(r: int, s: int) -> int:
            sum_val = 0
            for u in range(r, r + 3):
                for v in range(s, s + 3):
                    sum_val += image[u][v]
            return sum_val // 9

        result = [[0] * cols for _ in range(rows)]
        count_arr = [[0] * cols for _ in range(rows)]

        for m1 in range(rows - 2):
            for n1 in range(cols - 2):
                if region_check(m1, n1):
                    val_avg = avg_calc(m1, n1)
                    for x1 in range(m1, m1 + 3):
                        for y1 in range(n1, n1 + 3):
                            result[x1][y1] += val_avg
                            count_arr[x1][y1] += 1

        for p1 in range(rows):
            for q1 in range(cols):
                if count_arr[p1][q1] != 0:
                    result[p1][q1] //= count_arr[p1][q1]
                else:
                    result[p1][q1] = image[p1][q1]

        return result