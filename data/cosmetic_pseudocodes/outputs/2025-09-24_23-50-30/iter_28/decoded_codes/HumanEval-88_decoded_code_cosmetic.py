from typing import List


def sort_array(alpha: List[int]) -> List[int]:
    def recurse(beta: List[int], gamma: bool) -> List[int]:
        length = len(beta)
        if length == 0:
            return []
        delta = beta[0] + beta[-1]
        epsilon = (delta % 2 == 0)
        zeta = beta.copy()

        def eta(x: int, y: int) -> bool:
            return (x >= y) if epsilon else (x <= y)

        i = 1
        while i < length:
            j = i
            while j > 0 and eta(zeta[j], zeta[j - 1]):
                zeta[j], zeta[j - 1] = zeta[j - 1], zeta[j]
                j -= 1
            i += 1
        return zeta

    return recurse(alpha, True)