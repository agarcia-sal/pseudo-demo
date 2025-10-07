import math
from collections import defaultdict

def is_prime(p: int) -> bool:
    def check_divisor(q: int, r: int) -> bool:
        if p % q == 0:
            return False
        elif r == 0:
            return True
        else:
            return check_divisor(q + 6, r - 1)

    if p <= 1:
        return False
    elif p <= 3:
        return True
    elif (p % 2 == 0) or (p % 3 == 0):
        return False
    else:
        return check_divisor(5, int(math.isqrt(p)))


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        v1 = len(mat)
        if v1 == 0:
            return -1
        v2 = len(mat[0])
        if v2 == 0:
            return -1

        dlist = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                 (1, 0), (1, -1), (0, -1), (-1, -1)]
        tally = defaultdict(int)

        def walk(a: int, b: int, dx: int, dy: int, num: int):
            nx = a + dx
            ny = b + dy
            if 0 <= nx < v1 and 0 <= ny < v2:
                composed = num * 10 + mat[nx][ny]
                if composed > 10 and is_prime(composed):
                    tally[composed] += 1
                walk(nx, ny, dx, dy, composed)

        ci = 0
        while ci < v1:
            cj = 0
            while cj < v2:
                for dx, dy in dlist:
                    walk(ci, cj, dx, dy, mat[ci][cj])
                cj += 1
            ci += 1

        if not tally:
            return -1

        highest_prime = None
        highest_count = -1
        for k in tally:
            count = tally[k]
            if count > highest_count or (count == highest_count and (highest_prime is None or k < highest_prime)):
                highest_count = count
                highest_prime = k

        return highest_prime