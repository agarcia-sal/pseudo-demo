from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(array_of_items: Sequence[T]) -> bool:
    ascending_flag: bool = True
    descending_flag: bool = True
    cursor: int = 1
    length: int = len(array_of_items)
    while cursor < length:
        if array_of_items[cursor] < array_of_items[cursor - 1]:
            ascending_flag = False
        if array_of_items[cursor] > array_of_items[cursor - 1]:
            descending_flag = False
        cursor += 1
    return ascending_flag or descending_flag