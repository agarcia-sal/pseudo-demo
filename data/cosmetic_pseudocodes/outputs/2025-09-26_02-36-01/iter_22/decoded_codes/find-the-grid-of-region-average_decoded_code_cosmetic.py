from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])

        def is_valid_region(x: int, y: int) -> bool:
            delta_pairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for idx1 in range(3):
                for idx2 in range(3):
                    val1 = image[x + idx1][y + idx2]
                    for dx, dy in delta_pairs:
                        nx, ny = x + idx1 + dx, y + idx2 + dy
                        if x <= nx < x + 3 and y <= ny < y + 3:
                            val2 = image[nx][ny]
                            diff = val1 - val2
                            if diff * diff > threshold * threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            sum_accumulator = 0
            for row in range(3):
                for col in range(3):
                    sum_accumulator += image[x + row][y + col]
            return sum_accumulator // 9  # integer division for average

        matrix_accum = [[0] * cols for _ in range(rows)]
        matrix_counters = [[0] * cols for _ in range(rows)]

        for i_outer in range(rows - 2):
            for j_outer in range(cols - 2):
                if is_valid_region(i_outer, j_outer):
                    temp_avg = calculate_average(i_outer, j_outer)
                    for xi in range(3):
                        for yj in range(3):
                            pos_x, pos_y = i_outer + xi, j_outer + yj
                            matrix_accum[pos_x][pos_y] += temp_avg
                            matrix_counters[pos_x][pos_y] += 1

        for index_a in range(rows):
            for index_b in range(cols):
                if matrix_counters[index_a][index_b] > 0:
                    matrix_accum[index_a][index_b] //= matrix_counters[index_a][index_b]
                else:
                    matrix_accum[index_a][index_b] = image[index_a][index_b]

        return matrix_accum