from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    total_count = len(list_of_numbers)
    position_a = 0
    while position_a < total_count:
        value_a = list_of_numbers[position_a]
        position_b = 0
        while position_b < total_count:
            if position_a != position_b:
                dist = value_a - list_of_numbers[position_b]
                if dist < 0:
                    dist = -dist
                if dist < threshold_value:
                    return True
            position_b += 1
        position_a += 1
    return False