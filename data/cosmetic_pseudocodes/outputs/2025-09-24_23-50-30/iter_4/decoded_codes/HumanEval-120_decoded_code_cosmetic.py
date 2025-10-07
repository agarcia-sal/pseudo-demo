from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')


class Comparable:
    def __lt__(self: T, other: T) -> bool:
        ...


def maximum(arr: List[T], k: int) -> List[T]:
    if k == 0:
        return []
    sorted_arr = sorted(arr)
    return sorted_arr[-k:]