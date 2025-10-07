from typing import Callable


def largest_prime_factor(n: int) -> int:
    def is_prime(k: int) -> bool:
        def β(ω: int, ξ: int) -> bool:
            if ω <= 1:
                return False

            def µ(τ: int, ρ: int, σ: int) -> bool:
                if τ > ρ:
                    return True
                if k % τ == 0:
                    return False
                return µ(τ + 1, ρ, σ)

            return µ(2, k - 1, 0)

        return β(k, 0)

    def φ(alpha: int, υ: int) -> int:
        if alpha > n:
            return υ
        if n % alpha == 0 and is_prime(alpha):
            return φ(alpha_plus_one(alpha), max(υ, alpha))
        else:
            return φ(alpha_plus_one(alpha), υ)

    def alpha_plus_one(z: int) -> int:
        return z + 1

    return φ(2, 1)