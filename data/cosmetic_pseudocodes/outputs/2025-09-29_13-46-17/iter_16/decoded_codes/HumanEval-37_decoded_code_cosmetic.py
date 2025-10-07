from math import ceil, floor
from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def 𝔛𝑖(𝕬𝓸𝕃: List[T], 𝖸: int) -> List[T]:
        # Recursively take every second element starting at index 0
        if 𝖸 == 0:
            return []
        return [𝕬𝓸𝕃[0]] + 𝔛𝑖(𝕬𝓸𝕃[2:], 𝖸 - 1)

    ♾️₁ = 𝔛𝑖(list_of_elements, ceil(len(list_of_elements) / 2))
    Ɛ𝓪 = 𝔛𝑖(list_of_elements[1:], floor(len(list_of_elements) / 2))

    def 𝔖₢(ƹ: List[T]) -> List[T]:
        # Sort by swapping first two elements if out of order, recursively
        if len(ƹ) < 2:
            return ƹ
        h₁, h₂, T = ƹ[0], ƹ[1], ƹ[2:]
        if h₁ > h₂:
            return 𝔖₢([h₂, h₁] + T)
        return [h₁] + 𝔖₢([h₂] + T)

    v㉨ = 𝔖₢(♾️₁)

    def ⧓𝙳(a: int, b: int, c: List[T], d: List[T], acc: List[T]) -> List[T]:
        # Interleave elements from c and d into acc recursively
        if a < len(c):
            return ⧓𝙳(a + 1, b + 1, c, d, acc + [c[a], d[b]])
        return acc

    𝔏 = ⧓𝙳(0, 0, v㉨, Ɛ𝓪, [])

    if not (len(Ɛ𝓪) >= len(v㉨)):
        𝔏 += [v㉨[-1]]

    return 𝔏