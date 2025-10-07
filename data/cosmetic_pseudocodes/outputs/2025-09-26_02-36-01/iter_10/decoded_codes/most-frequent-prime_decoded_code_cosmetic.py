from typing import List, Dict

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    def check_div(k: int) -> bool:
        if k * k > n:
            return True
        if n % k == 0 or n % (k + 2) == 0:
            return False
        return check_div(k + 6)
    return check_div(5)

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        HORIZONTAL_VALUES = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        M = len(mat)
        if M == 0:
            return -1
        N = len(mat[0])
        if N == 0:
            return -1
        frequency_map: Dict[int, int] = {}

        def walk(x_pos: int, y_pos: int, delta_x: int, delta_y: int, accumulated: int) -> None:
            next_x = x_pos + delta_x
            next_y = y_pos + delta_y
            if next_x < 0 or next_x >= M:
                return
            if next_y < 0 or next_y >= N:
                return
            updated_num = accumulated * 10 + mat[next_x][next_y]
            if updated_num > 10 and is_prime(updated_num):
                frequency_map[updated_num] = frequency_map.get(updated_num, 0) + 1
            walk(next_x, next_y, delta_x, delta_y, updated_num)

        def row_iterate(row_idx: int) -> None:
            if row_idx == M:
                return
            def col_iterate(col_idx: int) -> None:
                if col_idx == N:
                    return
                def dir_iterate(dir_idx: int) -> None:
                    if dir_idx == len(HORIZONTAL_VALUES):
                        return
                    dx, dy = HORIZONTAL_VALUES[dir_idx]
                    walk(row_idx, col_idx, dx, dy, mat[row_idx][col_idx])
                    dir_iterate(dir_idx + 1)
                dir_iterate(0)
                col_iterate(col_idx + 1)
            col_iterate(0)
            row_iterate(row_idx + 1)

        row_iterate(0)

        if not frequency_map:
            return -1

        max_entry = None
        for key, value in frequency_map.items():
            if (max_entry is None
                or value > frequency_map[max_entry]
                or (value == frequency_map[max_entry] and key > max_entry)):
                max_entry = key
        return max_entry