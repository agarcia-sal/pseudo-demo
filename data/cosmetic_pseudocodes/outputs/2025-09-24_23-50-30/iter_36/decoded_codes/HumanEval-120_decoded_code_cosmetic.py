from typing import List, TypeVar

T = TypeVar('T')

def maximum(input_list: List[T], count: int) -> List[T]:
    if count <= 0:
        return []
    input_list.sort()
    start_index = len(input_list) - count
    return input_list[start_index:] if start_index >= 0 else input_list[:]