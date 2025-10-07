from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    local_list: List[T] = list(list_input)
    extracted_vals: List[T] = []
    idx: int = 0
    while idx < len(local_list):
        if idx % 3 == 0:
            extracted_vals.append(local_list[idx])
        idx += 1

    extracted_vals.sort()

    i: int = 0
    j: int = 0
    while i < len(local_list):
        if i % 3 == 0:
            local_list[i] = extracted_vals[j]
            j += 1
        i += 1

    return local_list