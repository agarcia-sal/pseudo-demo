from typing import List

def incr_list(list_of_elements: List[int]) -> List[int]:
    def β𝛂𝄞(ψ: List[int]) -> List[int]:
        return [] if not ψ else [ψ[0] + 1] + β𝛂𝄞(ψ[1:])

    def ζΘΦ(Κℓ: List[int]) -> List[int]:
        if not Κℓ:
            return []
        return [Κℓ[0] + 1] + ζΘΦ(Κℓ[1:])

    return ζΘΦ(list_of_elements)