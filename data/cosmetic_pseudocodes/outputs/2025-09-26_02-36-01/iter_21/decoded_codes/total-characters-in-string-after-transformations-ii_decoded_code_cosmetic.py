class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        mod_val = 10 ** 9 + 1  # 1,000,000,001

        def zero_matrix(rows: int, cols: int) -> list[list[int]]:
            def build_row(idx: int) -> list[int]:
                if idx < cols:
                    return [0] + build_row(idx + 1)
                else:
                    return []

            def build_matrix(ridx: int) -> list[list[int]]:
                if ridx < rows:
                    return [build_row(0)] + build_matrix(ridx + 1)
                else:
                    return []

            return build_matrix(0)

        trans_matrix = zero_matrix(26, 26)

        def increment_trans_matrix(x: int, y: int) -> None:
            trans_matrix[x][y] = (trans_matrix[x][y] + 1)

        def process_row(i: int, j: int) -> None:
            if j < nums[i]:
                idx = (i + j + 1) % 26
                increment_trans_matrix(i, idx)
                process_row(i, j + 1)

        def process_rows(i: int) -> None:
            if i < 26:
                process_row(i, 0)
                process_rows(i + 1)

        process_rows(0)

        def mat_mult(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            res = zero_matrix(26, 26)

            def mult_cell(i: int, j: int, k: int, acc: int) -> int:
                if k < 26:
                    return mult_cell(i, j, k + 1, (acc + (A[i][k] * B[k][j]) % mod_val) % mod_val)
                else:
                    return acc

            def fill_row(i: int, j: int) -> None:
                if j < 26:
                    res[i][j] = mult_cell(i, j, 0, 0)
                    fill_row(i, j + 1)

            def fill_matrix(i: int) -> None:
                if i < 26:
                    fill_row(i, 0)
                    fill_matrix(i + 1)

            fill_matrix(0)
            return res

        def identity_matrix(size: int) -> list[list[int]]:
            id_mat = zero_matrix(size, size)

            def set_identity(idx: int) -> None:
                if idx < size:
                    id_mat[idx][idx] = 1
                    set_identity(idx + 1)

            set_identity(0)
            return id_mat

        def mat_power(matrix: list[list[int]], power_: int) -> list[list[int]]:
            result = identity_matrix(26)
            base = matrix
            exp = power_

            def loop() -> None:
                nonlocal result, base, exp
                if exp > 0:
                    if (exp % 2) != 0:
                        result = mat_mult(result, base)
                    base = mat_mult(base, base)
                    exp //= 2
                    loop()

            loop()
            return result

        final_matrix = mat_power(trans_matrix, t)

        def count_chars(string: str) -> list[int]:
            cnt = [0] * 26

            def process_char(idx: int) -> None:
                if idx < len(string):
                    def char_to_index(c: str) -> int:
                        return ord(c) - ord('a')

                    pos = char_to_index(string[idx])
                    cnt[pos] += 1
                    process_char(idx + 1)

            process_char(0)
            return cnt

        current_count = count_chars(s)

        final_count = [0] * 26

        def update_final(i: int, j: int) -> None:
            if i < 26:
                if j < 26:
                    val = (final_count[j] + ((current_count[i] % mod_val) * (final_matrix[i][j] % mod_val))) % mod_val
                    final_count[j] = val
                    update_final(i, j + 1)
                else:
                    update_final(i + 1, 0)

        update_final(0, 0)

        def sum_list(lst: list[int], idx: int, acc: int) -> int:
            if idx < len(lst):
                return sum_list(lst, idx + 1, (acc + lst[idx]) % mod_val)
            else:
                return acc

        return sum_list(final_count, 0, 0)