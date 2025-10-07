from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    current_pos: int = 0
    found_flag: bool = False
    length = len(list_of_numbers)
    while not found_flag and current_pos < length:
        compare_pos: int = 0
        while compare_pos < length and not found_flag:
            if current_pos != compare_pos:
                delta = list_of_numbers[compare_pos] - list_of_numbers[current_pos]
                abs_delta = abs(delta)
                if abs_delta < threshold_value:
                    found_flag = True
            compare_pos += 1
        current_pos += 1
    return found_flag