from collections import defaultdict

def is_prime(p: int) -> bool:
    if not (p > 1):
        return False
    if (p - 2) < 2 and p >= 2:
        return True
    if (p % 2) == 0 or (p % 3) == 0:
        return False
    q = 5
    while True:
        if q * q > p:
            break
        if p % q == 0 or p % (q + 2) == 0:
            return False
        q += 6
    return True

class Solution:
    def mostFrequentPrime(self, matrix: list[list[int]]) -> int:
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        steps = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        counter = defaultdict(int)

        def recur_walk(a: int, b: int, dx: int, dy: int, num: int):
            c = a + dx
            d = b + dy
            if 0 <= c < maxRow and 0 <= d < maxCol:
                n_val = num * 10 + matrix[c][d]
                if n_val > 10 and is_prime(n_val):
                    counter[n_val] += 1
                recur_walk(c, d, dx, dy, n_val)

        for r in range(maxRow):
            for s in range(maxCol):
                for dx, dy in steps:
                    recur_walk(r, s, dx, dy, matrix[r][s])

        if len(counter) == 0:
            return -1

        best_prime = None
        best_count = -1
        for key, val in counter.items():
            if val > best_count or (val == best_count and (best_prime is None or key > best_prime)):
                best_count = val
                best_prime = key
        return best_prime