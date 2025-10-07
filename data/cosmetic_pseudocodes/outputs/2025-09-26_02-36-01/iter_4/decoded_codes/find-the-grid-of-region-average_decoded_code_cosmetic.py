from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows = len(image)
        columns = len(image[0]) if rows > 0 else 0

        accumulation = [[0] * columns for _ in range(rows)]
        occurrences = [[0] * columns for _ in range(rows)]

        def is_valid_region(x: int, y: int) -> bool:
            dxdy_pairs = [(-1,0), (1,0), (0,-1), (0,1)]
            limit_x = x + 3
            limit_y = y + 3
            for row_index in range(x, limit_x):
                for column_index in range(y, limit_y):
                    for offset_x, offset_y in dxdy_pairs:
                        neighbor_x = row_index + offset_x
                        neighbor_y = column_index + offset_y
                        if 0 <= neighbor_x < limit_x and 0 <= neighbor_y < limit_y:
                            difference = image[row_index][column_index] - image[neighbor_x][neighbor_y]
                            if abs(difference) > threshold:
                                return False
            return True

        def calculate_average(x: int, y: int) -> int:
            sum_accumulator = 0
            end_x = x + 3
            end_y = y + 3
            for outer_index in range(x, end_x):
                for inner_index in range(y, end_y):
                    sum_accumulator += image[outer_index][inner_index]
            divider = 9
            computed_average = sum_accumulator // divider
            return computed_average

        limit_i = rows - 2
        limit_j = columns - 2
        for main_i in range(limit_i):
            for main_j in range(limit_j):
                if is_valid_region(main_i, main_j):
                    avg_val = calculate_average(main_i, main_j)
                    for inner_x in range(main_i, main_i + 3):
                        for inner_y in range(main_j, main_j + 3):
                            accumulation[inner_x][inner_y] += avg_val
                            occurrences[inner_x][inner_y] += 1

        for idx_i in range(rows):
            for idx_j in range(columns):
                if occurrences[idx_i][idx_j] > 0:
                    numerator = accumulation[idx_i][idx_j]
                    denominator = occurrences[idx_i][idx_j]
                    accumulation[idx_i][idx_j] = numerator // denominator
                else:
                    accumulation[idx_i][idx_j] = image[idx_i][idx_j]

        return accumulation