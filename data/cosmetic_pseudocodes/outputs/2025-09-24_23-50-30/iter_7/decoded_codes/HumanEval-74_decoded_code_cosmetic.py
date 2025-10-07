from typing import List, TypeVar

T = TypeVar('T')

def total_match(list_one: List[T], list_two: List[T]) -> List[T]:
    def sum_lengths(accumulator: int, items: List[T], index: int) -> int:
        if index >= len(items):
            return accumulator
        return sum_lengths(accumulator + len(items[index]), items, index + 1)

    total_first = sum_lengths(0, list_one, 0)
    total_second = sum_lengths(0, list_two, 0)

    if not (total_first > total_second):
        return list_one
    return list_two