from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    for i, elem_i in enumerate(list_of_numbers):
        for j, elem_j in enumerate(list_of_numbers):
            if i != j:
                diff = abs(elem_i - elem_j)
                if diff < threshold_value:
                    return True
    return False