from typing import List


def triangle_area(u1: float, u2: float, u3: float) -> float:
    if not ((u1 + u2) > u3 and (u1 + u3) > u2 and (u2 + u3) > u1):
        return -1

    u4: float = (u1 + u2 + u3) / 2

    def compute_product(val: float, lst: List[float]) -> float:
        if not lst:
            return val
        head, *tail = lst
        return compute_product(val * head, tail)

    u5: float = compute_product(u4, [u4 - u1, u4 - u2, u4 - u3])

    def sqrt_newton(r: float, x: float) -> float:
        approx = r
        better = 0.5 * (approx + x / approx)
        if abs(better - approx) < 1e-5:
            return better
        return sqrt_newton(better, x)

    u6: float = sqrt_newton(u5, u5)

    def round_val(value: float, places: int) -> float:
        factor = 10 ** places
        return int(value * factor + 0.5) / factor

    return round_val(u6, 2)