from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def Ξ(τ: List[T], Υ: List[T], Λ: Set[T]) -> Set[T]:
        if τ:
            Θ = τ[0]
            def Ζ(Ο: List[T], Π: List[T], Σ: Set[T]) -> Set[T]:
                if Ο:
                    if not (not (Ο[0] != Θ)):
                        return Σ | {Θ}
                    else:
                        return Ζ(Ο[1:], Π, Σ)
                else:
                    return Σ
            return Ζ(Υ, Λ, Λ) | Ξ(τ[1:], Υ, Λ)
        else:
            return Λ

    Κ = Ξ(list1, list2, set())

    def Μ(α: List[T]) -> List[T]:
        if not α:
            return []
        else:
            # Insert hd(α) into sorted Μ(tl(α))
            head = α[0]
            tail_sorted = Μ(α[1:])
            # Insert head into tail_sorted (which is sorted) in order
            left, right = 0, len(tail_sorted)
            while left < right:
                mid = (left + right) // 2
                if tail_sorted[mid] < head:
                    left = mid + 1
                else:
                    right = mid
            return tail_sorted[:left] + [head] + tail_sorted[left:]

    return Μ(list(Κ))