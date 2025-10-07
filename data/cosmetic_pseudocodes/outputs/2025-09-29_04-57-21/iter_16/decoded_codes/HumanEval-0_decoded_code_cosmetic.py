from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for outer_idx in range(length):
        outer_val = list_of_numbers[outer_idx]
        for inner_idx in range(length):
            if outer_idx != inner_idx:
                diff = abs(outer_val - list_of_numbers[inner_idx])
                if diff < threshold_value:
                    return True
    return False