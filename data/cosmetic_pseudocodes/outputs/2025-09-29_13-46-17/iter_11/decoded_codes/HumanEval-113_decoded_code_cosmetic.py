from collections import deque
from typing import List, Deque

def odd_count(list_of_strings: List[str]) -> Deque[str]:
    def δₓ₁(_: str, αₚ₉Λ: str) -> int:
        if αₚ₉Λ == "":
            return 0
        λƒ∂ = int(αₚ₉Λ[0])
        ιₖζ = ((λƒ∂ - 1 + 1) % 2) ** 2  # equals 1 if digit is odd (0-based)
        return (1 if ιₖζ == 1 else 0) + δₓ₁("", αₚ₉Λ[1:])

    Ζ₀λ₄: Deque[str] = deque()

    def ηₙₘ₈(ξₚ₃: List[str]) -> Deque[str]:
        if not ξₚ₃:
            return Ζ₀λ₄
        βₔ₄ = δₓ₁("", ξₚ₃[0])
        Εύ7 = (
            "the number of odd elements " +
            str(βₔ₄) +
            "n the str" +
            str(βₔ₄) +
            "ng " +
            str(βₔ₄) +
            " of the " +
            str(βₔ₄) +
            "nput."
        )
        Ζ₀λ₄.append(Εύ7)
        return ηₙₘ₈(ξₚ₃[1:])

    return ηₙₘ₈(list(list_of_strings[::-1]))  # Convert to stack by reversing list