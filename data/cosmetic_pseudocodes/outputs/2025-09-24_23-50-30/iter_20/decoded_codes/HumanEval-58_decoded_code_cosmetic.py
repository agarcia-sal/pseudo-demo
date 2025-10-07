from typing import Iterable, List, TypeVar

T = TypeVar('T')

def common(a: Iterable[T], b: Iterable[T]) -> List[T]:
    accumulator: set[T] = set()
    index_x = 0
    a_list = list(a)
    b_list = list(b)
    while index_x < len(a_list):
        index_y = 0
        while index_y < len(b_list):
            if a_list[index_x] == b_list[index_y]:
                accumulator.add(a_list[index_x])
            index_y += 1
        index_x += 1
    return sorted(accumulator)