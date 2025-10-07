from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    local_list: List[T] = list(list_input)
    temp_collection: List[T] = []
    idx: int = 0

    while idx < len(local_list):
        if idx % 3 == 0:  # indices divisible by 3
            temp_collection.append(local_list[idx])
        idx += 1

    temp_idx: int = 0
    while temp_idx < len(temp_collection):
        current_min = temp_collection[temp_idx]
        swap_idx = temp_idx
        inner_idx = temp_idx + 1
        # Find the minimum element in the remainder of temp_collection
        while inner_idx < len(temp_collection):
            if temp_collection[inner_idx] < current_min:
                current_min = temp_collection[inner_idx]
                swap_idx = inner_idx
            inner_idx += 1
        if swap_idx != temp_idx:
            temp_collection[swap_idx], temp_collection[temp_idx] = temp_collection[temp_idx], current_min
        temp_idx += 1

    sorted_collection = temp_collection

    replace_idx = 0
    outer_idx = 0
    while outer_idx < len(local_list):
        if outer_idx % 3 == 0:
            local_list[outer_idx] = sorted_collection[replace_idx]
            replace_idx += 1
        outer_idx += 1

    return local_list