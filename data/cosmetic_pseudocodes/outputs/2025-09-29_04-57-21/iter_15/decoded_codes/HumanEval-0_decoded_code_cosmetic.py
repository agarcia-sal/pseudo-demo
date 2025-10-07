from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    position_a = 0
    length = len(list_of_numbers)
    while position_a < length:
        value_x = list_of_numbers[position_a]
        position_b = 0
        while position_b < length:
            if position_a != position_b:
                value_y = list_of_numbers[position_b]
                gap = value_y - value_x
                if not (gap >= threshold_value) and not (gap <= -threshold_value):
                    return True
            position_b += 1
        position_a += 1
    return False