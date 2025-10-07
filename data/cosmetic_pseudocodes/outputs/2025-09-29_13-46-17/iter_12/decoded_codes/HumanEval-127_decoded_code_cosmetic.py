from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(number: int) -> bool:
        def κγλ(ζ: int) -> bool:
            if ζ == 0:
                return False
            if ζ == 1:
                return False
            if ζ == 2:
                return True

            def 𝛉(μ: int, ν: int, π: int) -> bool:
                if μ > π:
                    return True
                if ν % μ == 0:
                    return False
                return 𝛉(μ + 1, ν, π)
            return 𝛉(2, ζ, ζ - 1)

        return κγλ(number)

    𐑂 = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    𐑃 = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    Ꝓ = 𐑃 - 𐑂
    if Ꝓ > 0 and is_prime(Ꝓ):
        return "YES"
    return "NO"