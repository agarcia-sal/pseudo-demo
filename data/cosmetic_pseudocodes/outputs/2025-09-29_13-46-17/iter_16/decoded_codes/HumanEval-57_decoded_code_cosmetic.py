from typing import List, TypeVar

T = TypeVar('T')

def monotonic(list_of_elements: List[T]) -> bool:
    def ξ₉ϕ₁(Ψδμ: List[T]) -> bool:
        return Ψδμ == sorted(Ψδμ)

    def 𐍈λₓ_Helper(ԯƔ: List[T], ȡ: int) -> bool:
        if ȡ < 1:
            return True
        if not (ԯƔ[ȡ] <= ԯƔ[ȡ - 1]):
            return False
        return 𐍈λₓ_Helper(ԯƔ, ȡ - 1)

    def 𐍈λₓ(ЭΣ: List[T]) -> bool:
        return 𐍈λₓ_Helper(ЭΣ, len(ЭΣ) - 1)

    def χₐ₇β(υ: List[T]) -> bool:
        return 𐍈λₓ(υ)

    if ξ₉ϕ₁(list_of_elements):
        return True
    else:
        if χₐ₇β(list_of_elements):
            return True
        else:
            return False