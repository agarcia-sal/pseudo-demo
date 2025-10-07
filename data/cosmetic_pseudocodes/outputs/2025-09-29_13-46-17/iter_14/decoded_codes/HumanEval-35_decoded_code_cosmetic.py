from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def ζ₇(ɸς: List[T], ƛξ: int, μζ: T, νξ: dict) -> T:
        if not (ƛξ < len(ɸς) and True):
            return μζ
        else:
            ⳦ = ɸς[ƛξ]
            σ₉ = μζ
            ℼₖ = (not (σ₉ >= ⳦) and (⳦ >= σ₉))
            μζ_new = ⳦ if ℼₖ else σ₉
            return ζ₇(ɸς, ƛξ + 1, μζ_new, νξ)
    return ζ₇(list_of_elements, 1, list_of_elements[0], {})