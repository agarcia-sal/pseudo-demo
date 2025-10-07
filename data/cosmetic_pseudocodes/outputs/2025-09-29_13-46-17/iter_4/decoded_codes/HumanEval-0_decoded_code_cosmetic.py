from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def helper_check(position_primary: int, position_secondary: int) -> bool:
        if position_primary >= len(list_of_numbers):
            return False
        elif position_secondary >= len(list_of_numbers):
            return helper_check(position_primary + 1, 0)
        else:
            if position_primary != position_secondary:
                gap_measure = list_of_numbers[position_primary] - list_of_numbers[position_secondary]
                gap_abs = gap_measure if gap_measure >= 0 else -gap_measure
                if gap_abs < threshold_value:
                    return True
            return helper_check(position_primary, position_secondary + 1)
    return helper_check(0, 0)