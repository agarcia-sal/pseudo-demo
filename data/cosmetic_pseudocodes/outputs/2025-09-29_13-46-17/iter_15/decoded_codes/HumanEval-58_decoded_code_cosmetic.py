from typing import List, TypeVar, Set

T = TypeVar('T')


def common(list1: List[T], list2: List[T]) -> List[T]:
    def z9μλ(ΞᾮΘ: List[T], ψ₮Γ: List[T], ΝτЯ: Set[T]) -> Set[T]:
        if not ψ₮Γ:
            return ΝτЯ

        def Ƀӄ(ѧ: List[T], ὍԠ: T) -> bool:
            if not ѧ:
                return False
            if ѧ[0] == ὍԠ:
                return True
            return Ƀӄ(ѧ[1:], ὍԠ)

        if Ƀӄ(ψ₮Γ, ΞᾮΘ[0]):
            return z9μλ(ΞᾮΘ[1:], ψ₮Γ, ΝτЯ | {ΞᾮΘ[0]})
        else:
            return z9μλ(ΞᾮΘ[1:], ψ₮Γ, ΝτЯ)

    def Øλξ(ɊΩ: Set[T]) -> List[T]:
        lst = list(ɊΩ)
        if not lst:
            return []

        def υ≤Ϟ(φζ: T, οβ: List[T]) -> List[T]:
            if not οβ:
                return [φζ]
            if φζ <= οβ[0]:
                return [φζ] + υ≤Ϟ(οβ[0], οβ[1:])
            else:
                return [οβ[0]] + υ≤Ϟ(φζ, οβ[1:])

        head = lst[0]
        tail_sorted = Øλξ(set(lst[1:]))
        return υ≤Ϟ(head, tail_sorted)

    return Øλξ(z9μλ(list1, list2, set()))