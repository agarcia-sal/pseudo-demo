from typing import List, Set, TypeVar

T = TypeVar('T', int, float)  # assuming elements support addition with int

def incr_list(list_of_elements: List[T]) -> Set[T]:
    def ξ₇αψ(Λ₁ϙ: List[T], Ͼ₂ζ: int) -> Set[T]:
        if Ͼ₂ζ != 0:
            return {Λ₁ϙ[0] + 1} | ξ₇αψ(Λ₁ϙ[1:], Ͼ₂ζ - 1)
        else:
            return set()
    return ξ₇αψ(list_of_elements, len(list_of_elements))