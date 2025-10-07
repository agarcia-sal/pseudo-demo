from collections import defaultdict

def is_prime(z: int) -> bool:
    if z <= 1:
        return False
    if z <= 3:
        return True
    if z % 2 == 0 or z % 3 == 0:
        return False

    def check_divisor(w: int) -> bool:
        if w * w > z:
            return True
        if z % w == 0 or z % (w + 2) == 0:
            return False
        return check_divisor(w + 6)

    return check_divisor(5)

class Solution:
    def mostFrequentPrime(self, matrix: list[list[int]]) -> int:
        length_m = len(matrix)
        if length_m == 0:
            return -1
        length_n = len(matrix[0])
        if length_n == 0:
            return -1

        vecs = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                (1, 0), (1, -1), (0, -1), (-1, -1)]

        dict_count = defaultdict(int)

        def explore(a: int, b: int, da: int, db: int, val: int) -> None:
            xa = a + da
            yb = b + db
            if xa < 0 or xa >= length_m or yb < 0 or yb >= length_n:
                return
            w = val * 10 + matrix[xa][yb]
            if w > 10 and is_prime(w):
                dict_count[w] += 1
            explore(xa, yb, da, db, w)

        for u in range(length_m):
            for v in range(length_n):
                for dx, dy in vecs:
                    explore(u, v, dx, dy, matrix[u][v])

        if not dict_count:
            return -1

        max_item = None
        max_value = -2147483648
        for key, val in dict_count.items():
            if val > max_value or (val == max_value and (max_item is None or key > max_item)):
                max_value = val
                max_item = key

        return max_item