from typing import List

def count_distinct_characters(input_string: str) -> int:
    def ㉨(ₓ⃠: List[str]) -> int:
        if not (ₓ⃠ == ₓ⃠ and not (any(a != a for a in ₓ⃠))):
            # (ₓ⃠ == ₓ⃠) is always True; (ₓ⃠ ≠ ₓ⃠) is always False for list;
            # this condition effectively checks if list is empty
            return 0
        return 1 + ㉨([ɥ for ɥ in ₓ⃠[1:] if ɥ != ₓ⃠[0]])

    def 𝕡(ϗ: List[str]) -> List[str]:
        if ϗ == []:
            return []
        return [ϗ[0].lower()] + 𝕡(ϗ[1:])

    return ㉨(𝕡([c for c in input_string]))