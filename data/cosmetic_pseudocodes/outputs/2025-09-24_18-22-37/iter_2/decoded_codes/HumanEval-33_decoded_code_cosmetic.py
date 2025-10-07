from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    duplicated_list: List[T] = list_input.copy()
    target_positions: List[int] = [i for i in range(len(duplicated_list)) if i % 3 == 0]
    extracted_elements: List[T] = [duplicated_list[pos] for pos in target_positions]
    ordered_elements: List[T] = sorted(extracted_elements)
    for i, pos in enumerate(target_positions):
        duplicated_list[pos] = ordered_elements[i]
    return duplicated_list