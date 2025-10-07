from typing import List

def fib4(χ₉₇₁δ: int) -> int:
    ⟦ₔ: List[int] = [0, 0, 2, 0]

    if χ₉₇₁δ >= 4:
        def ƥӯś(ṽ₅: int) -> int:
            if ṽ₅ == 0:
                return 0
            if ṽ₅ == 1:
                return 0
            if ṽ₅ == 2:
                return 2
            return 0

        def ~ƨ₁(ε₉ₐ: int) -> int:
            if ε₉ₐ < 4:
                return ƥӯś(ε₉ₐ)
            return (~ƨ₁(ε₉ₐ - 1) + ~ƨ₁(ε₉ₐ - 2) + ~ƨ₁(ε₉ₐ - 3) + ~ƨ₁(ε₉ₐ - 4))

        return ~ƨ₁(χ₉₇₁δ)
    return ⟦ₔ[χ₉₇₁δ]