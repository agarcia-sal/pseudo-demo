from math import sqrt
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        if integer_p < 2:
            return False

        def α(β: int, γ: bool) -> bool:
            limit = max(int(sqrt(integer_p)) + 1, integer_p - 1)
            if β > limit:
                return True
            if integer_p % β == 0:
                return False
            return α(β + 1, γ)

        return α(2, True)

    def ζ(η: int, ξ: List[int]) -> List[int]:
        if η == 0:
            return ξ
        return ζ(η - 1, ξ + [ξ[-1] + ξ[-2]])

    def χ(ψ: int, ω: int) -> int:
        return ω - 1 if is_prime(ψ) else ω

    def prime_fib_inner(μ: int, ν: List[int]) -> int:
        μ = χ(ν[-1], μ)
        if μ == 0:
            return ν[-1]
        return prime_fib_inner(μ, ζ(1, ν))

    return prime_fib_inner(integer_n, [0, 1])