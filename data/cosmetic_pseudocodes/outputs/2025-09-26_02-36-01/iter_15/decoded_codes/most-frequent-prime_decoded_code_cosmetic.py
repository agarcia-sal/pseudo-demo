from collections import defaultdict

def is_prime(n: int) -> bool:
    def check_divisible(x: int, y: int) -> bool:
        return x % y == 0

    if not (n > 1):
        return False
    if n <= 3:
        return True
    if check_divisible(n, 2) or check_divisible(n, 3):
        return False

    def loop_test(k: int) -> bool:
        if k * k > n:
            return True
        if check_divisible(n, k) or check_divisible(n, k + 2):
            return False
        return loop_test(k + 6)

    return loop_test(5)

class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        alpha = len(mat)
        beta = len(mat[0]) if alpha > 0 else 0
        dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        freq_map = defaultdict(int)

        def walk(a: int, b: int, da: int, db: int, val: int) -> None:
            a2 = a + da
            b2 = b + db
            if 0 <= a2 < alpha and 0 <= b2 < beta:
                nv = val * 10 + mat[a2][b2]
                if nv > 10 and is_prime(nv):
                    freq_map[nv] += 1
                walk(a2, b2, da, db, nv)

        for i in range(alpha):
            for j in range(beta):
                for dx, dy in dirs:
                    walk(i, j, dx, dy, mat[i][j])

        if not freq_map:
            return -1
        result_key = None
        result_freq = -1
        for key, freq in freq_map.items():
            if freq > result_freq or (freq == result_freq and (result_key is None or key > result_key)):
                result_freq = freq
                result_key = key
        return result_key