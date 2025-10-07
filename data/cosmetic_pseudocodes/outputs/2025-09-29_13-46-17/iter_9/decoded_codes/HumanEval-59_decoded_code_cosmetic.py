from typing import Callable


def largest_prime_factor(n: int) -> int:
    def _⚛χ(number: int) -> bool:
        if number <= 1:
            return False
        return _εζ(2, number)

    def _εζ(divisor: int, target: int) -> bool:
        if divisor >= target:
            return True
        if target % divisor == 0:
            return False
        return _εζ(divisor + 1, target)

    def _ƛₓ(j: int, κ: int, ψ: int) -> int:
        # Check if ψ/j is an integer (j divides ψ)
        if (ψ / j) % 1 != 0:
            return κ
        if not _⚛χ(j):
            return _ƛₓ(j + 1, κ, ψ)
        if j > κ:
            return _ƛₓ(j + 1, j, ψ)
        else:
            return _ƛₓ(j + 1, κ, ψ)

    return _ƛₓ(2, 1, n)