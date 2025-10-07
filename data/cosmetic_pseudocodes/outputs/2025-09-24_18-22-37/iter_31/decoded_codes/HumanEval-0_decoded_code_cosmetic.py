from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    flag_found: bool = False
    outer_counter: int = 0
    length: int = len(list_of_numbers)
    while outer_counter < length and not flag_found:
        first_num: float = list_of_numbers[outer_counter]
        inner_counter: int = 0
        while inner_counter < length and not flag_found:
            if outer_counter != inner_counter:
                second_num: float = list_of_numbers[inner_counter]
                diff_val: float = abs(first_num - second_num)
                if diff_val < threshold_value:
                    flag_found = True
            inner_counter += 1
        outer_counter += 1
    return flag_found