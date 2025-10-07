from typing import List

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        alpha = len(image)
        beta = len(image[0]) if alpha > 0 else 0
        omega = [[0 for _ in range(beta)] for _ in range(alpha)]
        psi = [[0 for _ in range(beta)] for _ in range(alpha)]

        def is_valid_region(x: int, y: int) -> bool:
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            def check_positions(a: int, b: int, c: int):
                if c == 4:
                    return
                nx = a + offsets[c][0]
                ny = b + offsets[c][1]
                if 0 <= nx < x + 3 and 0 <= ny < y + 3:
                    if abs(image[a][b] - image[nx][ny]) > threshold:
                        raise ValueError("INVALID")
                check_positions(a, b, c + 1)

            def check_rows(curr_i: int, end_i: int, curr_j: int, end_j: int):
                if curr_i == end_i:
                    return
                def inner_loop(curr_j_pos: int, limit_j: int):
                    if curr_j_pos == limit_j:
                        return
                    try:
                        check_positions(curr_i, curr_j_pos, 0)
                    except ValueError as e:
                        if str(e) == "INVALID":
                            raise
                        else:
                            raise
                    inner_loop(curr_j_pos + 1, limit_j)
                inner_loop(curr_j, end_j)
                check_rows(curr_i + 1, end_i, curr_j, end_j)

            try:
                check_rows(x, x + 3, y, y + 3)
            except ValueError as e:
                if str(e) == "INVALID":
                    return False
                else:
                    raise
            return True

        def calculate_average(x: int, y: int) -> int:

            def accumulate_row(i: int, j: int, limit_j: int) -> int:
                if j == limit_j:
                    return 0
                return image[i][j] + accumulate_row(i, j + 1, limit_j)

            def accumulate_col(i: int, limit_i: int, current_i: int) -> int:
                if current_i == limit_i:
                    return 0
                return accumulate_row(current_i, y, y + 3) + accumulate_col(i, limit_i, current_i + 1)

            sigma = accumulate_col(x, x + 3, x)
            epsilon = sigma // 9
            return epsilon

        def outer_loop(i: int, j: int):
            if i == alpha - 2:
                return
            def inner_loop_func(j_func: int):
                if j_func == beta - 2:
                    return
                if is_valid_region(i, j_func):
                    delta = calculate_average(i, j_func)
                    def assign_values(x_idx: int, y_idx: int):
                        if x_idx == i + 3:
                            return
                        def assign_inner(y_inner: int):
                            if y_inner == y_idx + 3:
                                return
                            omega[x_idx][y_inner] += delta
                            psi[x_idx][y_inner] += 1
                            assign_inner(y_inner + 1)
                        assign_inner(y_idx)
                        assign_values(x_idx + 1, y_idx)
                    assign_values(i, j_func)
                inner_loop_func(j_func + 1)
            inner_loop_func(j)
            outer_loop(i + 1, j)

        outer_loop(0, 0)

        def finalize_rows(i: int):
            if i == alpha:
                return
            def finalize_cols(j: int):
                if j == beta:
                    return
                if psi[i][j] > 0:
                    omega[i][j] = omega[i][j] // psi[i][j]
                else:
                    omega[i][j] = image[i][j]
                finalize_cols(j + 1)
            finalize_cols(0)
            finalize_rows(i + 1)

        finalize_rows(0)

        return omega