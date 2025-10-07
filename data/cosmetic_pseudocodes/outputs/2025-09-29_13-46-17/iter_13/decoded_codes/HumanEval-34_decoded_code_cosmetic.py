from typing import List, TypeVar

T = TypeVar("T")

def unique(list_of_elements: List[T]) -> List[T]:
    λ1 = set(list_of_elements)
    λ2 = list(λ1)

    def aux_ξ(ξ︀: List[T], υ₃: int) -> List[T]:
        if υ₃ == len(λ2):
            return ξ︀
        return aux_ξ(ξ︀ + [λ2[υ₃]], υ₃ + 1)

    𝛼 = aux_ξ([], 0)

    def sort_recursive(β₀: List[T]) -> List[T]:
        if not β₀:
            return []
        𝛽 = β₀[0]
        𝛾 = β₀[1:]
        less_eq = [x for x in 𝛾 if not (x < 𝛽)]
        less = [x for x in 𝛾 if x < 𝛽]
        return sort_recursive(less) + [𝛽] + sort_recursive(less_eq)

    return sort_recursive(𝛼)