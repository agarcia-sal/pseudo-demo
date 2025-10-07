from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_index: int = 0
    length: int = len(list_of_numbers)
    while outer_index < length:
        element_x: float = list_of_numbers[outer_index]
        inner_index: int = 0
        while inner_index < length:
            if outer_index != inner_index:
                element_y: float = list_of_numbers[inner_index]
                difference_calc: float = element_x - element_y
                if difference_calc < 0:
                    difference_calc = -difference_calc
                if difference_calc < threshold_value:
                    return True
            inner_index += 1
        outer_index += 1
    return False