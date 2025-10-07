from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pairs(current_pos: int, check_pos: int) -> bool:
        if current_pos > len(list_of_numbers):
            return False
        elif check_pos > len(list_of_numbers):
            return check_pairs(current_pos + 1, 1)
        else:
            if current_pos == check_pos:
                return check_pairs(current_pos, check_pos + 1)
            elif abs(list_of_numbers[current_pos - 1] - list_of_numbers[check_pos - 1]) < threshold_value:
                return True
            else:
                return check_pairs(current_pos, check_pos + 1)
    return check_pairs(1, 1)