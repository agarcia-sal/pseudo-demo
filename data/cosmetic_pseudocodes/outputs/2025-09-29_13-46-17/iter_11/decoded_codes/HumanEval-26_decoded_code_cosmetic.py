from typing import List, Set

def remove_duplicates(list_of_numbers: List[int]) -> List[int]:
    # Helper function: add element λχ to set ϗ if not present, else return ϗ as is.
    def ϱϜ(λχ: int, ϗ: Set[int]) -> Set[int]:
        if λχ not in ϗ:
            return ϗ | {λχ}
        else:
            return ϗ

    # Recursive function to build a set of unique elements from list Ω, starting with set 𝕐.
    def λττ(Ω: List[int], 𝕐: Set[int]) -> Set[int]:
        if not Ω:
            return 𝕐
        else:
            𝔪, *ξ𝕫 = Ω
            return λττ(ξ𝕫, ϱϜ(𝔪, 𝕐))

    # Return the set of unique elements from σλ
    def Ϟπ(σλ: List[int]) -> Set[int]:
        return λττ(σλ, set())

    ㊗: Set[int] = Ϟπ(list_of_numbers)

    # Recursive function to produce list without duplicates preserving order
    def ḥȢὊ(ψ: Set[int], ɮ: List[int]) -> List[int]:
        if not ɮ:
            return []
        else:
            𝖷, *ḃ = ɮ
            if 𝖷 not in ψ:
                return [𝖷] + ḥȢὊ(ψ | {𝖷}, ḃ)
            else:
                return ḥȢὊ(ψ, ḃ)

    return ḥȢὊ(set(), list_of_numbers)