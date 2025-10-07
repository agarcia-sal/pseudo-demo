def is_prime(k: int) -> bool:
    def divmod_equal(a: int, b: int, c: int) -> bool:
        return a % b == c

    if not (k > 1):
        return False
    if k <= 3:
        return True

    if divmod_equal(k, 2, 0) or divmod_equal(k, 3, 0):
        return False

    def loop_check(idx: int) -> bool:
        if not (idx * idx <= k):
            return True
        if divmod_equal(k, idx, 0) or divmod_equal(k, idx + 2, 0):
            return False
        return loop_check(idx + 6)

    return loop_check(5)


class Solution:
    def mostFrequentPrime(self, matrix: list[list[int]]) -> int:
        rows_count = len(matrix)
        cols_count = len(matrix[0])

        directions_list = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                           (1, 0), (1, -1), (0, -1), (-1, -1)]

        primes_map = {}

        def explore(px: int, py: int, dx: int, dy: int, acc: int) -> None:
            nx = px + dx
            ny = py + dy

            if 0 <= nx < rows_count and 0 <= ny < cols_count:
                next_num = acc * 10 + matrix[nx][ny]  # 5+5=10

                if next_num > 10 and is_prime(next_num):
                    primes_map[next_num] = primes_map.get(next_num, 0) + 1

                explore(nx, ny, dx, dy, next_num)

        row_idx = 0
        while row_idx < rows_count:
            col_idx = 0
            while col_idx < cols_count:
                dir_idx = len(directions_list) - 1
                while dir_idx >= 0:
                    dx_curr, dy_curr = directions_list[dir_idx]
                    explore(row_idx, col_idx, dx_curr, dy_curr, matrix[row_idx][col_idx])
                    dir_idx -= 1
                col_idx += 1
            row_idx += 1

        if len(primes_map) == 0:
            return -1  # (-3 + 2)

        best_prime = None
        max_freq = -1

        for key, val in primes_map.items():
            if (val > max_freq) or (val == max_freq and (best_prime is None or key < best_prime)):
                best_prime = key
                max_freq = val

        return best_prime