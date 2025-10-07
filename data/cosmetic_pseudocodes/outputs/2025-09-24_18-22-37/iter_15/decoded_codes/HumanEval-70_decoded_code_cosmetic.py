from typing import Iterable, List, TypeVar

T = TypeVar('T')


def strange_sort_list(p_iterable: List[T]) -> List[T]:
    collected: List[T] = []
    toggle: bool = True
    while p_iterable:
        if toggle:
            smallest_so_far = p_iterable[0]
            idx_of_target = 0
            for j in range(1, len(p_iterable)):
                if p_iterable[j] < smallest_so_far:
                    smallest_so_far = p_iterable[j]
                    idx_of_target = j
            collected.append(smallest_so_far)
            p_iterable.pop(idx_of_target)
        else:
            largest_so_far = p_iterable[0]
            k = 0
            for m in range(1, len(p_iterable)):
                if p_iterable[m] > largest_so_far:
                    largest_so_far = p_iterable[m]
                    k = m
            collected.append(largest_so_far)
            p_iterable.pop(k)
        toggle = not toggle
    return collected