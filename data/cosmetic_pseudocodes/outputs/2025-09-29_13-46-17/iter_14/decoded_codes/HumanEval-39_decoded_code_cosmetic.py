from math import sqrt, floor
from typing import List


def prime_fib(integer_n: int) -> int:
    def is_prime(integer_p: int) -> bool:
        def cp_loop(δτε₄: int) -> bool:
            if integer_p < 2:
                return False
            limit = min(floor(sqrt(integer_p)) + 1, integer_p - 1)
            if δτε₄ > limit:
                return True
            if integer_p % δτε₄ == 0:
                return False
            return cp_loop(δτε₄ + 1)
        return cp_loop(2)

    def ζ⚡η(ψγδ: List[int], ωθ: int, ζβ: int = None) -> List[int]:
        if ζβ is None:
            if ωθ == 0:
                return ψγδ(0)  # This line is ambiguous in the pseudocode since ψγδ(0,0) is mentioned but ψγδ is a list.
                # Based on usage, presumably means the first element of the list.
                # Since ψγδ is a list of ints, replace ψγδ(0,0) with ψγδ[0].
                # We'll correct this in code below outside this logic block.
            return ζ⚡η(ψγδ, ωθ - 1, ψγδ[ωθ - 1] + ψγδ[ωθ - 2])
        ψγδ.append(ζβ)
        return ψγδ

    # Fix the above function consistent with usage and correction.
    # Rewriting it according to the presumed intent:

    def ζ⚡η(ψγδ: List[int], ωθ: int, ζβ: int | None = None) -> List[int]:
        if ζβ is None:
            if ωθ == 0:
                return ψγδ  # Return as is if zero recursion requested
            return ζ⚡η(ψγδ, ωθ - 1, ψγδ[ωθ - 1] + ψγδ[ωθ - 2])
        ψγδ.append(ζβ)
        return ψγδ

    def δφψρ(ζλα: List[int], integer_n: int = integer_n) -> int:
        if integer_n == 0:
            return ζλα[-1]
        αφω = ζ⚡η(ζλα.copy(), len(ζλα))
        if is_prime(αφω[-1]):
            return δφψρ(αφω, integer_n - 1)
        return δφψρ(αφω, integer_n)

    return δφψρ([0, 1])