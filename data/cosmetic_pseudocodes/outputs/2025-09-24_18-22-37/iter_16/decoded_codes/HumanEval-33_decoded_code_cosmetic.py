from typing import List, Any

def sort_third(array_elements: List[Any]) -> List[Any]:
    copied_sequence: List[Any] = array_elements.copy()
    divisible_by_three_elements: List[Any] = []
    idx: int = 0
    while idx < len(copied_sequence):
        if idx % 3 == 0:
            divisible_by_three_elements.append(copied_sequence[idx])
        idx += 1

    sorted_subset: List[Any] = sorted(divisible_by_three_elements)

    target_index: int = 0
    iter_: int = 0
    while iter_ < len(copied_sequence):
        if iter_ % 3 == 0:
            copied_sequence[iter_] = sorted_subset[target_index]
            target_index += 1
        iter_ += 1

    return copied_sequence