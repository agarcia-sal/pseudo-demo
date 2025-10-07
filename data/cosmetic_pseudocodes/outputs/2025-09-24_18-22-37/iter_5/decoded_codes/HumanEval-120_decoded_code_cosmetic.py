from typing import List, TypeVar

T = TypeVar('T')


def maximum(input_list: List[T], count: int) -> List[T]:
    if count == 0:
        return []
    input_list.sort()
    length_of_list = len(input_list)
    start_index = length_of_list - count
    return input_list[start_index:length_of_list]