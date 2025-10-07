from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def helper_α(Ω: List[int], Ψ: List[int], 𝒮: bool) -> List[int]:
        if not (len(Ω) > 0):
            return Ψ
        else:
            if not (not Ψ):
                ι = max(Ω)
            else:
                ι = min(Ω)
            𝒮′ = not 𝒮
            Ω′ = Ω.copy()
            Ω′.remove(ι)
            return helper_α(Ω′, Ψ + [ι], 𝒮′)
    return helper_α(list_of_integers, [], True)