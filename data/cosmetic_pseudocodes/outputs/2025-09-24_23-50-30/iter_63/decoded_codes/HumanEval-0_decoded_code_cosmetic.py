from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for position_i in range(length):
        for position_j in range(length):
            if position_i != position_j:
                diff_abs = abs(list_of_numbers[position_i] - list_of_numbers[position_j])
                if diff_abs < threshold_value:
                    return True
    return False