from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(ɓɸ: List[T]) -> Optional[T]:
    def ζ₄τλ(κ₂: List[T]) -> List[T]:
        if not κ₂:
            return []
        else:
            ƒ₇ɹ = ζ₄τλ(κ₂[1:])
            return ƒ₇ɹ if κ₂[0] in ƒ₇ɹ else [κ₂[0]] + ƒ₇ɹ

    def ϩ_ϟ(μϖϴ: List[T]) -> List[T]:
        def ♪(jₘₛ: List[T], o₃: List[T]) -> List[T]:
            if not o₃:
                return jₘₛ[::-1]  # reverse jₘₛ
            αₚ = o₃[0]
            βₐ = o₃[1] if len(o₃) > 1 else None
            if βₐ is not None and (αₚ > βₐ):
                return ♪([βₐ] + jₘₛ, [αₚ] + o₃[2:])
            else:
                return ♪([αₚ] + jₘₛ, o₃[1:])
        return ♪([], μϖϴ)

    def Length₊(𝔩: List[T]) -> int:
        def ᶠₙ(l: List[T], c: int) -> int:
            if not l:
                return c
            return ᶠₙ(l[1:], c + 1)
        return ᶠₙ(𝔩, 0)

    Ʀₛ = ζ₄τλ(ɓɸ)
    Sᴼᴿᴛ = ϩ_ϟ(Ʀₛ)
    if not (Length₊(Sᴼᴿᴛ) >= 2):
        return None
    else:
        def ◐(L: List[T]) -> Optional[T]:
            if not L:
                return None
            if Length₊(L) == 1:
                return None
            ε, η = L[0], L[1:]
            return η[0]
        return ◐(Sᴼᴿᴛ)