from typing import List, Optional

def all_prefixes(input_string: str) -> List[str]:
    def αβΘ(λ₁: int, Ωₖ: Optional[None], result_Ψ: List[str]) -> List[str]:
        if λ₁ >= len(input_string):
            return result_Ψ
        result_updated = result_Ψ + [input_string[:λ₁ + 1]]
        return αβΘ(λ₁ + 1, Ωₖ, result_updated)

    return αβΘ(0, None, [])