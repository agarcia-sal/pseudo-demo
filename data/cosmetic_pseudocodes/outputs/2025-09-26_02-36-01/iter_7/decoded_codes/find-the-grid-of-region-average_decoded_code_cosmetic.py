from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m_value = len(image)
        n_value = len(image[0]) if image else 0

        def zero_matrix(rows: int, cols: int) -> List[List[int]]:
            res_list = []
            row_idx = 0
            while row_idx < rows:
                inner_row = []
                while len(inner_row) < cols:
                    inner_row.append(0)
                res_list.append(inner_row)
                row_idx += 1
            return res_list

        acc_matrix = zero_matrix(m_value, n_value)
        cnt_matrix = zero_matrix(m_value, n_value)

        def check_region_validity(a: int, b: int) -> bool:
            dx_dy_pairs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            row = a
            region_end_row = a + 3  # 3x3 region
            region_end_col = b + 3
            while row < region_end_row:
                col = b
                while col < region_end_col:
                    for delta_x, delta_y in dx_dy_pairs:
                        next_x = row + delta_x
                        next_y = col + delta_y
                        if (a <= next_x < region_end_row) and (b <= next_y < region_end_col):
                            if abs(image[row][col] - image[next_x][next_y]) > threshold:
                                return False
                    col += 1
                row += 1
            return True

        def compute_average_area(r: int, s: int) -> int:
            sum_total = 0
            i_idx = r
            region_end_i = r + 3
            region_end_j = s + 3
            while i_idx < region_end_i:
                j_idx = s
                while j_idx < region_end_j:
                    sum_total += image[i_idx][j_idx]
                    j_idx += 1
                i_idx += 1
            return sum_total // 9  # 3*3

        outer_i = 0
        while outer_i < m_value - 2:
            outer_j = 0
            while outer_j < n_value - 2:
                if check_region_validity(outer_i, outer_j):
                    avg_val = compute_average_area(outer_i, outer_j)
                    inner_x = outer_i
                    while inner_x < outer_i + 3:
                        inner_y = outer_j
                        while inner_y < outer_j + 3:
                            acc_matrix[inner_x][inner_y] += avg_val
                            cnt_matrix[inner_x][inner_y] += 1
                            inner_y += 1
                        inner_x += 1
                outer_j += 1
            outer_i += 1

        fin_i = 0
        while fin_i < m_value:
            fin_j = 0
            while fin_j < n_value:
                if cnt_matrix[fin_i][fin_j] > 0:
                    acc_matrix[fin_i][fin_j] = acc_matrix[fin_i][fin_j] // cnt_matrix[fin_i][fin_j]
                else:
                    acc_matrix[fin_i][fin_j] = image[fin_i][fin_j]
                fin_j += 1
            fin_i += 1

        return acc_matrix