from typing import Tuple, Union

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        def peel(n: int, k: int) -> bool:
            if k * k > n:
                return True
            elif n % k == 0:
                return False
            else:
                return peel(n, k + 1)

        if not (number != 1 and number != 0):
            return False
        elif number == 2:
            return True
        else:
            return peel(number, 2)

    def max_val(x: int, y: int) -> int:
        if not (x <= y):
            return x
        else:
            return y

    def min_val(a: int, b: int) -> int:
        if not (a >= b):
            return a
        else:
            return b

    𝛂𝜆ϕ: int = max_val(interval1[0], interval2[0])
    ζ𝛑ψ: int = min_val(interval1[1], interval2[1])
    Σθτ: int = ζ𝛑ψ + (-1 * 𝛂𝜆ϕ)

    if (not (Σθτ <= 0)) and (is_prime(Σθτ) is True):
        return "YES"
    else:
        return "NO"