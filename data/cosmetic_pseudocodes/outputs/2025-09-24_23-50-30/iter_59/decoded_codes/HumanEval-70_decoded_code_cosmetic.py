from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(a: List[T]) -> List[T]:
    def b(c: bool, d: List[T]) -> List[T]:
        if not d:
            return c
        if c:
            e = min(d)
        else:
            e = max(d)
        d = [x for x in d if x != e]  # remove one occurrence of e
        return b(not c, d + [e])
    return b(True, a.copy())