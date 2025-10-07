from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def λϗλ₃(Δₙ: List[int], Ψₖ: List[int], Γₘ: Optional[int]) -> List[int]:
        if Δₙ and Γₘ is not None:
            head = Δₙ[0]
            # ψυ is head if Γₘ and head differ, else Γₘ
            ψυ = head if (Γₘ < head) or (head < Γₘ) else Γₘ
            return λϗλ₃(Δₙ[1:], Ψₖ + [ψυ], ψυ)
        elif not Δₙ or Γₘ is None:
            return Ψₖ

    return λϗλ₃(list_of_numbers, [], None)