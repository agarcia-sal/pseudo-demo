from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    duplicate_list = list(list_input)
    filtered_elements: List[T] = [duplicate_list[i] for i in range(len(duplicate_list)) if i % 3 == 0]
    ordered_subset = sorted(filtered_elements)
    position_counter = 0
    for idx in range(len(duplicate_list)):
        if idx % 3 == 0:
            duplicate_list[idx] = ordered_subset[position_counter]
            position_counter += 1
    return duplicate_list