from collections import defaultdict

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if 2 <= n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    h = 5
    while h * h <= n:
        if n % h == 0 or n % (h + 2) == 0:
            return False
        h += 6
    return True

class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        p = len(mat)
        if p == 0:
            return -1
        q = len(mat[0])
        if q == 0:
            return -1

        moves = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        prime_count = defaultdict(int)

        def traverse(a: int, b: int, dx: int, dy: int, val: int) -> None:
            x_next = a + dx
            y_next = b + dy
            if 0 <= x_next < p and 0 <= y_next < q:
                value_new = val * 10 + mat[x_next][y_next]
                if value_new > 10 and is_prime(value_new):
                    prime_count[value_new] += 1
                traverse(x_next, y_next, dx, dy, value_new)

        for row in range(p):
            for col in range(q):
                for dx, dy in moves:
                    traverse(row, col, dx, dy, mat[row][col])

        if not prime_count:
            return -1

        max_pair = (-1, -1)
        result = -1
        for key in prime_count:
            candidate = (prime_count[key], key)
            if candidate > max_pair:
                max_pair = candidate
                result = key
        return result