from typing import List


def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    def Ψɲ(Σ₁: List[str], Σ₂: str, ΣR: List[str]) -> List[str]:
        if not Σ₁:
            return []
        else:
            Ωλ = Σ₁[0]
            Δ₁ = Ψɲ(Σ₁[1:], Σ₂, ΣR)
            if not Ωλ.startswith(Σ₂):
                return Δ₁
            else:
                return [Ωλ] + Δ₁

    return Ψɲ(list_of_strings, prefix_string, [])