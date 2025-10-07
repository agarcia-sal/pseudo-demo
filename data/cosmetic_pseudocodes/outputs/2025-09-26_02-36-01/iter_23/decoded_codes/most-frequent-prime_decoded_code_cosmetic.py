def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    def check_divisor(d, val):
        if val * val > n:
            return True
        if n % val == 0 or n % (val + 2) == 0:
            return False
        return check_divisor(d, val + 6)

    return check_divisor(6, 5)


class Solution:
    def mostFrequentPrime(self, mat):
        L1 = len(mat)
        L2 = len(mat[0])
        delta_list = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]
        counts_map = {}

        def recurse_traverse(X, Y, DX, DY, current_val):
            NXT_X = X + DX
            NXT_Y = Y + DY
            if 0 <= NXT_X < L1 and 0 <= NXT_Y < L2:
                composed_num = current_val * 10 + mat[NXT_X][NXT_Y]
                if composed_num > 10 and is_prime(composed_num):
                    counts_map[composed_num] = counts_map.get(composed_num, 0) + 1
                recurse_traverse(NXT_X, NXT_Y, DX, DY, composed_num)

        def loop_rows(row_idx):
            if row_idx >= L1:
                return

            def loop_cols(col_idx):
                if col_idx >= L2:
                    return

                def process_dirs(dir_idx):
                    if dir_idx >= len(delta_list):
                        return
                    dx_val, dy_val = delta_list[dir_idx]
                    recurse_traverse(row_idx, col_idx, dx_val, dy_val, mat[row_idx][col_idx])
                    process_dirs(dir_idx + 1)

                process_dirs(0)
                loop_cols(col_idx + 1)

            loop_cols(0)
            loop_rows(row_idx + 1)

        loop_rows(0)

        if not counts_map:
            return -1

        max_freq_prime = None
        max_freq = 0

        def find_max_key(keys, idx):
            nonlocal max_freq_prime, max_freq
            if idx >= len(keys):
                return max_freq_prime
            k = keys[idx]
            v = counts_map[k]
            if v > max_freq:
                max_freq = v
                max_freq_prime = k
            return find_max_key(keys, idx + 1)

        all_keys = list(counts_map.keys())
        find_max_key(all_keys, 0)

        return max_freq_prime