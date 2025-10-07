from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    copied_list: List[T] = list(list_input)
    divisible_indices_values: List[T] = [copied_list[idx] for idx in range(0, len(copied_list), 3)]
    temp_sorted_values: List[T] = list(divisible_indices_values)
    temp_sorted_values.sort()
    replace_idx = 0
    for write_idx in range(len(copied_list)):
        if write_idx % 3 == 0:
            copied_list[write_idx] = temp_sorted_values[replace_idx]
            replace_idx += 1
    return copied_list