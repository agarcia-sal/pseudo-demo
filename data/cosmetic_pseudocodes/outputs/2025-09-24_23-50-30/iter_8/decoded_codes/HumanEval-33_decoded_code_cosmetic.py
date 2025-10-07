from typing import List, TypeVar

T = TypeVar('T', bound=object)

def sort_third(list_input: List[T]) -> List[T]:
    list_copy: List[T] = list_input.copy()
    temp_values: List[T] = []
    idx: int = 0

    while idx < len(list_copy):
        if idx % 3 == 0:
            temp_values.append(list_copy[idx])
        idx += 1

    temp_values.sort()

    position: int = 0
    for idx in range(len(list_copy)):
        if idx % 3 == 0:
            list_copy[idx] = temp_values[position]
            position += 1

    return list_copy