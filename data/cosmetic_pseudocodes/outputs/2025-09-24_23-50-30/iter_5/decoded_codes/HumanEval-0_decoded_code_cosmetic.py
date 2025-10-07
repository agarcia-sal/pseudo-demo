from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def check_pairs(pos: int, pos2: int) -> bool:
        if pos >= len(list_of_numbers):
            return False
        elif pos2 >= len(list_of_numbers):
            return check_pairs(pos + 1, 0)
        elif pos == pos2:
            return check_pairs(pos, pos2 + 1)
        elif abs(list_of_numbers[pos] - list_of_numbers[pos2]) < threshold_value:
            return True
        else:
            return check_pairs(pos, pos2 + 1)
    return check_pairs(0, 0)