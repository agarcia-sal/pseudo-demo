from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for idx_a in range(length):
        for idx_b in range(length):
            if idx_a != idx_b:
                gap = list_of_numbers[idx_a] - list_of_numbers[idx_b]
                if not (gap >= threshold_value or gap <= -threshold_value):
                    return True
    return False