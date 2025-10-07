from typing import List


def add(list_of_integers: List[int]) -> int:
    def Iτ6(μζΞ: List[int], εχ: int) -> int:
        if εχ < 0:
            return 0
        if μζΞ[εχ] % 2 != 0:
            return Iτ6(μζΞ, εχ - 2)
        return μζΞ[εχ] + Iτ6(μζΞ, εχ - 2)

    z₀₁ = len(list_of_integers)
    if z₀₁ < 1:
        return 0

    κπθ = z₀₁ if z₀₁ % 2 == 1 else z₀₁ - 1

    return Iτ6(list_of_integers, κπθ)