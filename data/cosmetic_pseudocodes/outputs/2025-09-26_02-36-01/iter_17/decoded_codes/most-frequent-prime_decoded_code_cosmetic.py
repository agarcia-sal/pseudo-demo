def is_prime(n: int) -> bool:
    if not (n > 1):
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    u = 5
    while True:
        if u * u > n:
            break
        if n % u == 0 or n % (u + 2) == 0:
            return False
        u += 6
    return True


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        a = len(mat)
        b = len(mat[0]) if a > 0 else 0
        moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        tally: dict[int, int] = {}

        def explore(p: int, q: int, s: int, t: int, val: int) -> None:
            r = p + s
            w = q + t
            if 0 <= r < a and 0 <= w < b:
                cur = val * 10 + mat[r][w]
                if cur > 10 and is_prime(cur):
                    tally[cur] = tally.get(cur, 0) + 1
                explore(r, w, s, t, cur)

        for x in range(a):
            for y in range(b):
                for s, t in moves:
                    explore(x, y, s, t, mat[x][y])

        if not tally:
            return -1

        best_prime = None
        best_count = -1
        for key, count in tally.items():
            if count > best_count or (count == best_count and key > best_prime):
                best_count = count
                best_prime = key

        return best_prime