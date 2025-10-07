from typing import List, TypeVar, Sequence

T = TypeVar('T')
S = TypeVar('S')

def intersperse(p_array: Sequence[T], p_sep: S) -> List:
    temp_result: List = []
    temp_length: int = len(p_array)

    if not (temp_length > 0):
        return []

    temp_index: int = 1
    while temp_index < temp_length:
        temp_result.append(p_array[temp_index])
        temp_result.append(p_sep)
        temp_index += 1

    temp_result.append(p_array[temp_length - 1])
    return temp_result