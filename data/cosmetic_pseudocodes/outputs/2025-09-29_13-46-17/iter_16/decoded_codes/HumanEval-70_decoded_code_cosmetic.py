from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def ψ(xυδ: List[int], χ: bool) -> List[int]:
        if not xυδ:
            return []
        if χ:
            ζ = min(xυδ)
        else:
            ζ = max(xυδ)
        κ = xυδ.copy()
        κ.remove(ζ)  # remove first occurrence
        return [ζ] + ψ(κ, not χ)
    return ψ(list_of_integers, True)