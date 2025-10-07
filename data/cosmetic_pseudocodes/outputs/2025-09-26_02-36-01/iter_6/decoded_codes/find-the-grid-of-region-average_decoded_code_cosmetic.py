from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        alpha = len(image)
        beta = len(image[0]) if image else 0

        def replicate_row(length_val: int) -> List[int]:
            return [0] * length_val

        output_matrix = []
        freq_matrix = []
        for _ in range(alpha):
            output_matrix.append(replicate_row(beta))
            freq_matrix.append(replicate_row(beta))

        def is_valid_region(x: int, y: int) -> bool:
            def neighbor_offsets() -> List[tuple[int, int]]:
                return [(-1, 0), (1, 0), (0, -1), (0, 1)]

            limit_i = x + 3
            def i_loop(index: int) -> bool:
                if index >= limit_i:
                    return True

                limit_j = y + 3
                def j_loop(inner_index: int) -> bool:
                    if inner_index >= limit_j:
                        return True

                    diffs = neighbor_offsets()
                    def check_offsets(offset_idx: int) -> bool:
                        if offset_idx >= len(diffs):
                            return True

                        dx, dy = diffs[offset_idx]
                        nx_val = index + dx
                        ny_val = inner_index + dy
                        if not (0 <= nx_val < x + 3 and 0 <= ny_val < y + 3):
                            return check_offsets(offset_idx + 1)

                        c_left = abs(image[index][inner_index] - image[nx_val][ny_val])
                        if c_left > threshold:
                            return False
                        return check_offsets(offset_idx + 1)

                    if not check_offsets(0):
                        return False
                    else:
                        return j_loop(inner_index + 1)

                if not j_loop(y):
                    return False
                else:
                    return i_loop(index + 1)

            return i_loop(x)

        def calculate_average(x: int, y: int) -> int:
            def sum_recursive(x_pos: int, i_pos: int, acc: int) -> int:
                if x_pos >= x + 3:
                    return acc
                if i_pos >= y + 3:
                    return sum_recursive(x_pos + 1, y, acc)
                new_acc = acc + image[x_pos][i_pos]
                return sum_recursive(x_pos, i_pos + 1, new_acc)

            final_sum = sum_recursive(x, y, 0)
            nine_val = 9
            return final_sum // nine_val

        outer_i = 0
        while outer_i < alpha - 2:
            outer_j = 0
            while outer_j < beta - 2:
                if is_valid_region(outer_i, outer_j):
                    average_val = calculate_average(outer_i, outer_j)
                    fill_x = outer_i
                    while fill_x < outer_i + 3:
                        fill_y = outer_j
                        while fill_y < outer_j + 3:
                            out_current = output_matrix[fill_x][fill_y]
                            freq_current = freq_matrix[fill_x][fill_y]
                            output_matrix[fill_x][fill_y] = out_current + average_val
                            freq_matrix[fill_x][fill_y] = freq_current + 1
                            fill_y += 1
                        fill_x += 1
                outer_j += 1
            outer_i += 1

        cnt_i = 0
        while cnt_i < alpha:
            cnt_j = 0
            while cnt_j < beta:
                freq_val = freq_matrix[cnt_i][cnt_j]
                if freq_val > 0:
                    output_matrix[cnt_i][cnt_j] = output_matrix[cnt_i][cnt_j] // freq_val
                else:
                    output_matrix[cnt_i][cnt_j] = image[cnt_i][cnt_j]
                cnt_j += 1
            cnt_i += 1

        return output_matrix