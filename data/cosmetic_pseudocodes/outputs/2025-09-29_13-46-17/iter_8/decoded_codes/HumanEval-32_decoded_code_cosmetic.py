from typing import List, Tuple, Callable


def poly(list_of_coefficients: List[float], point: float) -> float:
    def foldFun(acc: float, pair: Tuple[float, int]) -> float:
        coeff, idx = pair

        def expPow(base: float, power: int, acc: float) -> float:
            if power < 1:
                return acc
            else:
                return expPow(base, power - 1, acc * base)

        return acc + coeff * expPow(point, idx, 1)

    return foldFun(
        0,
        (pair for pair in zip(list_of_coefficients, range(len(list_of_coefficients)))),
    )


def find_zero(list_of_coefficients: List[float]) -> float:
    def checkSign(x: float, y: float) -> bool:
        return poly(list_of_coefficients, x) * poly(list_of_coefficients, y) > 0

    def scaleBounds(beg: float, en: float) -> Tuple[float, float]:
        if checkSign(beg, en):
            return scaleBounds(beg * 2.0, en * 2.0)
        else:
            return (beg, en)

    def bisect(lo: float, hi: float) -> float:
        if (hi - lo) <= 1e-10:
            return lo
        mid = (lo + hi) / 2.0
        if poly(list_of_coefficients, mid) * poly(list_of_coefficients, lo) > 0:
            return bisect(mid, hi)
        else:
            return bisect(lo, mid)

    startBound, endBound = scaleBounds(-1.0, 1.0)
    return bisect(startBound, endBound)