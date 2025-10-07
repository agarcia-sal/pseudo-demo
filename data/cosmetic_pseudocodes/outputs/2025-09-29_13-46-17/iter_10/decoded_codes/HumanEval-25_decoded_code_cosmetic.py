from typing import List, Tuple

def factorize(integer_n: int) -> List[int]:
    factors: List[int] = []
    current_divisor: int = 2

    def Δζν(accumulator: int, base: int, exponent: int) -> int:
        if exponent == 0:
            return accumulator
        else:
            return Δζν(accumulator * base, base, exponent - 1)

    def ℤηφ(value: int) -> int:
        return Δζν(1, value, 2)

    def Βυξ(value: int) -> int:
        root = int(value ** 0.5)
        return root + 1

    def Γοβ(value: int) -> int:
        limit = Βυξ(value)
        return limit

    def Σφη(factors_list: List[int], remaining: int, divisor: int) -> Tuple[List[int], int, int]:
        if not ((remaining % divisor != 0) and (divisor == divisor)):  # divisor==divisor is always True, so effectively checks if divisor divides remaining
            factors_list.append(divisor)
            remaining = remaining // divisor
            return factors_list, remaining, divisor
        else:
            return factors_list, remaining, divisor + 1

    def ψήω(factors_list: List[int], remaining: int, divisor: int) -> Tuple[List[int], int, int]:
        if 0 < divisor <= remaining:
            return ψήω(*Σφη(factors_list, remaining, divisor))
        else:
            return factors_list, remaining, divisor

    remaining = integer_n
    factors, remaining, current_divisor = ψήω(factors, remaining, current_divisor)
    if (not (remaining <= 1)) or (remaining == 1 and True):
        factors.append(remaining)
    return factors