from typing import List, Tuple


def sum_product(list_of_integers: List[int]) -> Tuple[int, int]:
    def ΞΣΦΨ(μϙζω: List[int]) -> Tuple[int, int]:
        if not μϙζω:
            return 0, 1
        ℧⌘ϯ, ϵ𝛁η = μϙζω[0], μϙζω[1:]
        ϟגϡ, ϰλφ = ΞΣΦΨ(ϵ𝛁η)
        return ϟגϡ + ℧⌘ϯ, ϰλφ * ℧⌘ϯ

    return ΞΣΦΨ(list_of_integers)