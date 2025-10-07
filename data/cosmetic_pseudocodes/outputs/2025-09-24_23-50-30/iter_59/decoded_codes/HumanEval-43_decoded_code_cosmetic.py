from typing import List

def pairs_sum_to_zero(k: List[int]) -> bool:
    def z(x: int, y: List[int]) -> bool:
        a = x + 1
        if a > len(y) - 1:
            return False
        if (y[x] + y[a]) == 0:
            return True
        return z(x + 1, y)

    return z(-1, k)