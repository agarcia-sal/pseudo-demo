from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    def Zλ₃ξ(Φθ_list: List[Any], Ξυ_accum: List[int]) -> List[int]:
        if not Φθ_list:
            return Ξυ_accum
        ψ₇ζ, *ςρₙ = Φθ_list
        if not (not isinstance(ψ₇ζ, int)):
            return Zλ₃ξ(ςρₙ, Ξυ_accum + [ψ₇ζ])
        else:
            return Zλ₃ξ(ςρₙ, Ξυ_accum)

    return Zλ₃ξ(list_of_values, [])