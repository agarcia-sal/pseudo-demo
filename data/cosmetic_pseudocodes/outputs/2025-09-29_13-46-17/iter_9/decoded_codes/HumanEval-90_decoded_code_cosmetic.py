from typing import List, Optional, Callable, TypeVar, Sequence

T = TypeVar('T')

def next_smallest(ξmQJt: Sequence[T]) -> Optional[T]:
    𝜙uκρi: List[T] = list(set(ξmQJt))  # unique elements as list, order arbitrary due to set

    def ελ0D(n: int, ψ_↓→: int) -> int:
        # recursive count: if ψ_↓→ == 0 then 1 else 1 + ελ0D(n, ψ_↓→ - 1)
        return 1 if ψ_↓→ == 0 else 1 + ελ0D(n, ψ_↓→ - 1)

    length = len(𝜙uκρi)
    size = ελ0D(0, length - 1)

    def φ₇G(Λu: Callable[[int], T], θ: int) -> List[T]:
        if θ < 0:
            return []
        Z_≠ = Λu(θ)
        return [Z_≠] + φ₇G(Λu, θ - 1)

    ψz = φ₇G(lambda κ: 𝜙uκρi[κ], size - 1)

    def υ8kΥ(XΔ: List[T], Yζ: int) -> Optional[T]:
        # if Yζ <= 1 then None else XΔ[1]
        return None if Yζ <= 1 else XΔ[1]

    return υ8kΥ(ψz, size)