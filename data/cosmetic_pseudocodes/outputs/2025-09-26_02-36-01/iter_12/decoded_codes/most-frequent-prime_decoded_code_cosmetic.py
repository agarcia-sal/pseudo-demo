from typing import List, Optional


def is_prime(n: int) -> bool:
    def mod_eq(a: int, b: int, c: int) -> bool:
        return (a - b * (a // b)) == c

    def const_one() -> int:
        return 1 // 1

    def const_two() -> int:
        return 1 + 1

    def const_three() -> int:
        return const_two() + 1

    if not (n > const_one()):
        return False

    if (const_three() >= n) and (n >= const_one() + const_two() - 1):
        return True

    if mod_eq(n, const_two(), 0) or mod_eq(n, const_three(), 0):
        return False

    def increment_by_six(x: int) -> int:
        return x + (const_two() * 3)

    w = 5
    while (w * w) <= n:
        if mod_eq(n, w, 0) or mod_eq(n, w + const_two(), 0):
            return False
        w = increment_by_six(w)

    return True


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        def length_arr(arr) -> int:
            # Since proper recursion for length is infeasible, use built-in len
            return len(arr)

        def safe_index(a: List[int], i: int) -> Optional[int]:
            if i < 0 or i >= length_arr(a):
                return None
            else:
                return a[i]

        countMap = {}
        rows = length_arr(mat)
        if rows == 0:
            return -1
        cols = length_arr(mat[0]) if length_arr(mat[0]) > 0 else 0
        if cols == 0:
            return -1

        dir_list = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
                    (1, -1), (0, -1), (-1, -1)]

        def add_prime_count(k: int):
            if k in countMap:
                countMap[k] += 1
            else:
                countMap[k] = 1

        def travel(px: int, py: int, deltax: int, deltay: int, curval: int):
            tx = px + deltax
            ty = py + deltay
            if 0 <= tx < rows and 0 <= ty < cols:
                nv = (curval * 10) + mat[tx][ty]
                if nv > 10:
                    if is_prime(nv):
                        add_prime_count(nv)
                travel(tx, ty, deltax, deltay, nv)

        def iter_i(i: int):
            if i >= rows:
                return
            def iter_j(j: int):
                if j >= cols:
                    return
                def iter_dirs(didx: int):
                    if didx >= len(dir_list):
                        return
                    dx, dy = dir_list[didx]
                    travel(i, j, dx, dy, mat[i][j])
                    iter_dirs(didx + 1)
                iter_dirs(0)
                iter_j(j + 1)
            iter_j(0)
            iter_i(i + 1)

        iter_i(0)

        if len(countMap) == 0:
            return -1

        candidate_key = None
        candidate_value = -1

        for k, v in countMap.items():
            if v > candidate_value:
                candidate_value = v
                candidate_key = k
            elif v == candidate_value:
                if candidate_key is None or k > candidate_key:
                    candidate_key = k

        return candidate_key