from typing import List, TypeVar, Callable

T = TypeVar('T')


def intersperse(lst: List[T], sep: T) -> List[T]:
    def helper(i: int, xs: List[T], j: int) -> List[T]:
        if i > j:
            return []
        next_i = i + 1
        tail = helper(next_i, xs, j)
        if next_i == j:
            head = [xs[i]]
        else:
            head = [xs[i], sep]
        return head + tail

    if len(lst) == 0:
        return []
    return helper(0, lst, len(lst) - 1)