from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    duplicate_list: List[T] = list_input[:]
    positions_divisible_by_three: List[int] = []
    extracted_elements: List[T] = []
    idx: int = 0
    while idx < len(duplicate_list):
        if idx % 3 == 0:
            positions_divisible_by_three.append(idx)
            extracted_elements.append(duplicate_list[idx])
        idx += 1

    extracted_elements.sort()  # sort extracted elements in ascending order

    replace_idx: int = 0
    while replace_idx < len(positions_divisible_by_three):
        position = positions_divisible_by_three[replace_idx]
        duplicate_list[position] = extracted_elements[replace_idx]
        replace_idx += 1

    return duplicate_list