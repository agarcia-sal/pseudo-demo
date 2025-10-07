from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    def calc_length(lst: List[T], idx: int, acc: int) -> int:
        if idx == len(lst):
            return acc
        return calc_length(lst, idx + 1, acc + len(lst[idx]))

    size_one: int = calc_length(list_one, 0, 0)
    size_two: int = calc_length(list_two, 0, 0)

    if size_one <= size_two:
        return list_one
    return list_two