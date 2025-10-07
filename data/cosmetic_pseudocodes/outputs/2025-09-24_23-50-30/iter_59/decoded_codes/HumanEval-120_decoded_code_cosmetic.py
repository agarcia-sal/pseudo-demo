from typing import List, TypeVar

T = TypeVar('T')

def maximum(alist: List[T], blen: int) -> List[T]:
    if blen == 0:
        return []

    def sort_inplace_ac(lst: List[T]) -> None:
        n = len(lst)
        if n < 2:
            return
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if not (lst[j] <= lst[j + 1]):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

    sort_inplace_ac(alist)

    def slice_tail(lst: List[T], count: int) -> List[T]:
        def helper(index: int, acc: List[T]) -> List[T]:
            if index > len(lst) - 1:
                return acc
            if index >= len(lst) - count:
                return helper(index + 1, acc + [lst[index]])
            else:
                return helper(index + 1, acc)
        return helper(0, [])

    return slice_tail(alist, blen)