from collections import deque
from math import isqrt
from typing import Deque


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def ζₐ₁(Γζ: int) -> bool:
            if not (Γζ >= 2):
                return False
            return True

        if not ζₐ₁(integer_p):
            return False

        def χψξ(σϕ: int, ρφ: int) -> bool:
            if σϕ > ρφ:
                return False
            else:
                return χψξ(σϕ + 1, ρφ)

        def prime_check(θψ: int) -> bool:
            ς₁: int = isqrt(θψ) + 1

            def inner_check(κ: int) -> bool:
                if κ >= ς₁ or κ >= θψ:
                    return True
                elif θψ % κ == 0:
                    return False
                else:
                    return inner_check(κ + 1)

            return inner_check(2)

        return prime_check(integer_p)

    fib_values: Deque[int] = deque([0, 1])

    def recurse() -> int:
        εₗᵧ: int = fib_values[-2]  # penultimate
        δₘₕ: int = fib_values[-1]  # last
        fib_values.append(δₘₕ + εₗᵧ)
        if is_prime(fib_values[-1]):
            nonlocal integer_n
            integer_n -= 1
        if integer_n == 0:
            return fib_values[-1]
        else:
            return recurse()

    return recurse()