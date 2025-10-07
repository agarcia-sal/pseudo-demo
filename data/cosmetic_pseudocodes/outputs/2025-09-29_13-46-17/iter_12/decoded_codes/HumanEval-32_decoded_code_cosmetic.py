from typing import List

def poly(coeffs: List[float], x: float) -> float:
    def Π(base: float, limit: int, acc: float, current: int) -> float:
        if current == limit:
            return acc
        return Π(base, limit, base * acc, current + 1)

    total: float = 0.0
    i: int = 0
    length: int = len(coeffs)
    while i < length:
        total += coeffs[i] * Π(x, i, 1.0, 0)
        i += 1
    return total

def find_zero(coeffs: List[float], _theta: float) -> float:
    def Θ(c: List[float], val: float) -> float:
        return poly(c, val)

    left: float = -1.0
    right: float = 1.0

    while True:
        prod = Θ(coeffs, left) * Θ(coeffs, right)
        if not (prod <= 0 or prod == 0):  # prod > 0
            left += left
            right += right
        else:
            break

    while (right - left) > 1e-10:
        mid = (left + right) / 2.0
        mid_prod = Θ(coeffs, mid) * Θ(coeffs, left)
        if mid_prod > 0:
            left = mid
        else:
            right = mid

    return left