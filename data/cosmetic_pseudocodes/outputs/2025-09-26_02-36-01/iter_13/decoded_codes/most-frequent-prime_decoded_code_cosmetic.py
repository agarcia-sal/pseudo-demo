from typing import List, Tuple, Dict

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while True:
        if i * i > n:
            break
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        r_len = len(mat)
        c_len = len(mat[0]) if r_len > 0 else 0
        dirs_list: List[Tuple[int, int]] = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        prime_map: Dict[int, int] = {}

        def rec_traverse(posx: int, posy: int, stepx: int, stepy: int, acc_num: int) -> None:
            next_x = posx + stepx
            next_y = posy + stepy
            if 0 <= next_x < r_len and 0 <= next_y < c_len:
                new_val = acc_num * 10 + mat[next_x][next_y]  # 5+5=10, so multiply acc_num by 10 and add next cell
                if new_val > 10 and is_prime(new_val):
                    prime_map[new_val] = prime_map.get(new_val, 0) + 1
                rec_traverse(next_x, next_y, stepx, stepy, new_val)

        for outer_i in range(r_len):
            for outer_j in range(c_len):
                for dx, dy in dirs_list:
                    rec_traverse(outer_i, outer_j, dx, dy, mat[outer_i][outer_j])

        if not prime_map:
            return -1

        max_count = -1
        result_key = -1
        for key, count in prime_map.items():
            if count > max_count or (count == max_count and key > result_key):
                max_count = count
                result_key = key
        return result_key