from typing import List, Optional, TypeVar

T = TypeVar('T')


def median(list_of_elements: List[T]) -> Optional[float | T]:
    def EXTRACT(σ: List[T], α: int, β: int) -> List[T]:
        if α >= β:
            return []
        return [σ[α]] + EXTRACT(σ, α + 1, β)

    def HEAD(σ: List[T]) -> Optional[T]:
        return σ[0] if σ else None

    def SORT(ξ: List[T]) -> List[T]:
        if len(ξ) <= 1:
            return ξ
        a = ξ[0]
        less = SORT([x for x in ξ[1:] if x < a])
        greater_equal = SORT([x for x in ξ[1:] if not x < a])
        return less + [a] + greater_equal

    def kz7χr(ɸσ: List[T]) -> Optional[float | T]:
        length = len(ɸσ)
        if not (length % 2 == 1):  # even length
            return (kz7χr(EXTRACT(ɸσ, 0, length // 2)) + kz7χr(EXTRACT(ɸσ, length // 2, length))) / 2.0
        else:
            if length == 1:
                return HEAD(ɸσ)
            return kz7χr(EXTRACT(ɸσ, length // 2, length // 2 + 1))

    return kz7χr(SORT(list_of_elements))