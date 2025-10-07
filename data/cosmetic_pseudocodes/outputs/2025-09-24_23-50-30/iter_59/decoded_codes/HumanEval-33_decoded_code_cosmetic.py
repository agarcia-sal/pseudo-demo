from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_third(a: Sequence[T]) -> List[T]:
    def helper(i: int, b: List[T], c: List[T]) -> List[T]:
        if i >= len(b):
            return c
        if i % 3 == 0:
            return helper(i + 1, b, c + [b[i]])
        else:
            return helper(i + 1, b, c)

    def replacer(i: int, b: List[T], d: List[T], e: int) -> List[T]:
        if i >= len(b):
            return b
        if i % 3 == 0:
            b[i] = d[e]
            return replacer(i + 1, b, d, e + 1)
        else:
            return replacer(i + 1, b, d, e)

    a_list = list(a)
    f = helper(0, a_list, [])
    g = sorted(f)
    return replacer(0, a_list, g, 0)