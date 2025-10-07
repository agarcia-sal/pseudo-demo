from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    primary_pos: int = 0
    length: int = len(list_of_numbers)
    while primary_pos < length:
        primary_num: float = list_of_numbers[primary_pos]
        secondary_pos: int = 0
        while secondary_pos < length:
            if primary_pos != secondary_pos:
                gap: float = primary_num - list_of_numbers[secondary_pos]
                if -threshold_value < gap < threshold_value:
                    return True
            secondary_pos += 1
        primary_pos += 1
    return False