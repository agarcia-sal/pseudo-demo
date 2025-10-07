from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    list_length: int = len(list_of_numbers)
    a_counter: int = 0
    while a_counter < list_length:
        first_elem: float = list_of_numbers[a_counter]
        b_counter: int = 0
        while True:
            if b_counter == list_length:
                break
            if a_counter != b_counter:
                diff_val: float = first_elem - list_of_numbers[b_counter]
                if diff_val < 0:
                    diff_val = -diff_val
                if diff_val < threshold_value:
                    return True
            b_counter += 1
        a_counter += 1
    return False