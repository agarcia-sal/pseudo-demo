from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    count_numbers = len(list_of_numbers)
    position_alpha = 0
    while position_alpha < count_numbers:
        element_alpha = list_of_numbers[position_alpha]
        position_beta = 0
        while position_beta < count_numbers:
            if position_alpha != position_beta:
                element_beta = list_of_numbers[position_beta]
                abs_diff = element_alpha - element_beta
                if abs_diff < 0:
                    abs_diff = -abs_diff
                if abs_diff < threshold_value:
                    return True
            position_beta += 1
        position_alpha += 1
    return False