class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONST_MOD = 10**9 + 1

        matrix_transform = [[0] * 26 for _ in range(26)]

        def proc_fill_transform(i_curr: int, j_curr: int) -> None:
            if i_curr == 26:
                return
            if j_curr == nums[i_curr]:
                proc_fill_transform(i_curr + 1, 0)
            else:
                idx_target = (i_curr + j_curr + 1) % 26
                matrix_transform[i_curr][idx_target] += 1
                proc_fill_transform(i_curr, j_curr + 1)

        proc_fill_transform(0, 0)

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            accumulator = [[0] * 26 for _ in range(26)]

            def multiply_cells(x: int, y: int, z: int, running_sum: int) -> int:
                if z == 26:
                    return running_sum % CONST_MOD
                product_val = (A[x][z] * B[z][y]) % CONST_MOD
                return multiply_cells(x, y, z + 1, (running_sum + product_val) % CONST_MOD)

            def fill_row(i_idx: int, j_idx: int) -> None:
                if i_idx == 26:
                    return
                if j_idx == 26:
                    fill_row(i_idx + 1, 0)
                else:
                    accumulator[i_idx][j_idx] = multiply_cells(i_idx, j_idx, 0, 0)
                    fill_row(i_idx, j_idx + 1)

            fill_row(0, 0)
            return accumulator

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            id_mat = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base_mat = matrix

            def power_iter(exp: int, res_mat: list[list[int]], base_mat_inner: list[list[int]]) -> list[list[int]]:
                if exp == 0:
                    return res_mat
                if exp % 2 != 0:
                    res_mat = matrix_multiply(res_mat, base_mat_inner)
                base_mat_inner = matrix_multiply(base_mat_inner, base_mat_inner)
                return power_iter(exp // 2, res_mat, base_mat_inner)

            return power_iter(power, id_mat, base_mat)

        powered_matrix = matrix_power(matrix_transform, t)

        count_letters = [0] * 26

        def count_chars(index: int) -> None:
            if index == len(s):
                return
            ch_val = ord(s[index]) - ord('a')
            count_letters[ch_val] += 1
            count_chars(index + 1)

        count_chars(0)

        output_counts = [0] * 26

        def compute_final(i_outer: int, j_inner: int) -> None:
            if i_outer == 26:
                return
            if j_inner == 26:
                compute_final(i_outer + 1, 0)
            else:
                prod_val = (count_letters[i_outer] * powered_matrix[i_outer][j_inner]) % CONST_MOD
                output_counts[j_inner] = (output_counts[j_inner] + prod_val) % CONST_MOD
                compute_final(i_outer, j_inner + 1)

        compute_final(0, 0)

        sum_total = 0

        def sum_values(idx: int) -> int:
            nonlocal sum_total
            if idx == 26:
                return sum_total
            sum_total = (sum_total + output_counts[idx]) % CONST_MOD
            return sum_values(idx + 1)

        return sum_values(0)