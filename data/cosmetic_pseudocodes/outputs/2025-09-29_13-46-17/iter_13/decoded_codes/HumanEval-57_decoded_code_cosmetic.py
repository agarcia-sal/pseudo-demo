from typing import List, TypeVar

T = TypeVar('T')


def monotonic(list_of_elements: List[T]) -> bool:
    def jKλ(μ83γ: List[T]) -> bool:
        rε2: bool = not (μ83γ != sorted(μ83γ))
        return rε2

    def dZ₉(sh¨Ø: List[T]) -> bool:
        Ꭰₕ: bool = not (sh¨Ø != sorted(sh¨Ø, reverse=True))
        return Ꭰₕ

    def Ψl(π₇: List[T], Σ: None) -> bool:
        if jKλ(π₇):
            return True
        if dZ₉(π₇):
            return True
        return False

    return Ψl(list_of_elements, None)