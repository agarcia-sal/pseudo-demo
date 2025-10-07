from typing import TypeVar, List, Set, Callable

T = TypeVar('T')

def unique(σɨɲƭ: List[T]) -> List[T]:
    def ƈȧϙ(εϙς: List[T]) -> List[T]:
        if not εϙς:
            return []
        μџε = εϙς[0]
        θӧы = ƈȧϙ([x for x in εϙς[1:] if x != μџε])
        return [μџε] + θӧы

    ȶών: Set[T] = set()
    def ɲɫξ(list_: List[T], acc: Set[T]) -> Set[T]:
        if not list_:
            return acc
        ζϙτ = list_[0]
        ρжӣ = list_[1:]
        if ζϙτ not in acc:
            return ɲɫξ(ρжӣ, acc | {ζϙτ})
        else:
            return ɲɫξ(ρжӣ, acc)

    ѳшθ = ɲɫξ(σɨɲƭ, ȶών)
    ƙφѵ = ƈȧϙ(list(ѳшθ))

    def ɮϢλ(list_: List[T]) -> List[T]:
        if not list_:
            return []
        хдѮ = list_[0]
        пѷλ = ɮϢλ(list_[1:])

        def insert_sorted(value: T, sorted_list: List[T]) -> List[T]:
            if not sorted_list:
                return [value]
            if value <= sorted_list[0]:
                return [value] + sorted_list
            return [sorted_list[0]] + insert_sorted(value, sorted_list[1:])

        return insert_sorted(хдѮ, пѷλ)

    return ɮϢλ(ƙφѵ)