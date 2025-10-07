from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        alpha = len(image)
        beta = len(image[0]) if alpha > 0 else 0
        delta = [[0] * beta for _ in range(alpha)]
        omega = [[0] * beta for _ in range(alpha)]

        def is_valid_region(u: int, v: int) -> bool:
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            flag = True
            p = u
            while p < u + 3:
                q = v
                while q < v + 3:
                    for dx, dy in offsets:
                        r = p + dx
                        s = q + dy
                        if 0 <= r < u + 3 and 0 <= s < v + 3:
                            if abs(image[p][q] - image[r][s]) > threshold:
                                flag = False
                                # Exit both loops immediately
                                return False
                    q += 1
                p += 1
            return flag

        def calculate_average(g: int, h: int) -> int:
            sum_value = 0
            for m_idx in range(g, g + 3):
                for n_idx in range(h, h + 3):
                    sum_value += image[m_idx][n_idx]
            return sum_value // 9  # integer division

        outer_index = 0
        while outer_index < alpha - 2:
            inner_index = 0
            while inner_index < beta - 2:
                if is_valid_region(outer_index, inner_index):
                    computed_avg = calculate_average(outer_index, inner_index)
                    x_idx = outer_index
                    while x_idx < outer_index + 3:
                        y_idx = inner_index
                        while y_idx < inner_index + 3:
                            delta[x_idx][y_idx] += computed_avg
                            omega[x_idx][y_idx] += 1
                            y_idx += 1
                        x_idx += 1
                inner_index += 1
            outer_index += 1

        a = 0
        while a < alpha:
            b = 0
            while b < beta:
                if omega[a][b] > 0:
                    delta[a][b] = delta[a][b] // omega[a][b]
                else:
                    delta[a][b] = image[a][b]
                b += 1
            a += 1

        return delta