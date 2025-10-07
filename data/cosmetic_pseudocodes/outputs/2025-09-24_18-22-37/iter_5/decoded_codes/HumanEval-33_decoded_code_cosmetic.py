from typing import List, Any


def sort_third(list_input: List[Any]) -> List[Any]:
    auxiliary_list: List[Any] = list_input.copy()
    divisible_indices: List[int] = []
    gathered_elements: List[Any] = []

    current_index: int = 0
    while current_index < len(auxiliary_list):
        if current_index % 3 == 0:
            divisible_indices.append(current_index)
            gathered_elements.append(auxiliary_list[current_index])
        current_index += 1

    gathered_elements.sort()

    position: int = 0
    while position < len(divisible_indices):
        auxiliary_list[divisible_indices[position]] = gathered_elements[position]
        position += 1

    return auxiliary_list