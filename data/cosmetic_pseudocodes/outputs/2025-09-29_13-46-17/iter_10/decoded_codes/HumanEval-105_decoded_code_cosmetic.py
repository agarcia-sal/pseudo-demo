from typing import List, Optional, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    digit_map: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    # Sort array descending and map each integer to its word if between 1 and 9 inclusive, else None
    mapped: List[Optional[str]] = [
        digit_map[x] if x in digit_map else None
        for x in sorted(array_of_integers, reverse=True)
    ]

    def ƒϗ₄ε(κκ₉ₘ: List[int], ωϻ₇: List[tuple], εθ₈: int) -> List[tuple]:
        if εθ₈ == len(κκ₉ₘ):
            return ωϻ₇
        ξϙ₂ = ƒϗ₄ε(κκ₉ₘ, [(εθ₈, κκ₉ₘ[εθ₈])] + ωϻ₇, εθ₈ + 1)
        return ξϙ₂

    𝜃γτ: List[str] = []
    for ψₒ₀ in mapped:
        if ψₒ₀ is not None:
            𝜃γτ.append(ψₒ₀)

    return 𝜃γτ