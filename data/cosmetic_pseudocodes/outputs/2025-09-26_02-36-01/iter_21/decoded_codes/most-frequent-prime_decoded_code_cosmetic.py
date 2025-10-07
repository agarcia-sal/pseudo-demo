from typing import List, Dict, Tuple, Optional

def is_prime(alpha: int) -> bool:
    if alpha <= 1:
        return False
    if alpha <= 3:
        return True
    if alpha % 2 == 0 or alpha % 3 == 0:
        return False

    def recur(delta: int) -> bool:
        if delta * delta > alpha:
            return True
        if alpha % delta == 0 or alpha % (delta + 2) == 0:
            return False
        return recur(delta + 6)

    return recur(5)


class Solution:
    def mostFrequentPrime(self, mu: List[List[int]]) -> int:
        nu = len(mu)
        if nu == 0:
            return -1
        xi = len(mu[0])
        omega: List[Tuple[int, int]] = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
        sigma: Dict[int, int] = {}

        def walk(a1: int, a2: int, a3: int, a4: int, a5: int) -> None:
            b1 = a1 + a3
            b2 = a2 + a4
            if 0 <= b1 < nu and 0 <= b2 < xi:
                c1 = (a5 * 10) + mu[b1][b2]
                if c1 > 10 and is_prime(c1):
                    sigma[c1] = sigma.get(c1, 0) + 1
                walk(b1, b2, a3, a4, c1)

        i = 0
        while i < nu:
            j = 0
            while j < xi:
                idx = 0
                while idx < len(omega):
                    dx, dy = omega[idx]
                    walk(i, j, dx, dy, mu[i][j])
                    idx += 1
                j += 1
            i += 1

        if len(sigma) == 0:
            return -1

        result: Optional[int] = None
        max_pair = (-1, -1)  # (frequency, prime)
        for key in sigma.keys():
            current_pair = (sigma[key], key)
            if current_pair[0] > max_pair[0] or (current_pair[0] == max_pair[0] and current_pair[1] > max_pair[1]):
                max_pair = current_pair
                result = key
        return result if result is not None else -1