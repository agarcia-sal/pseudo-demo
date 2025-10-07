from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    # Check if the input list is empty
    flag_empty: bool = True
    index_checker: int = 0
    while index_checker < len(array_of_integers) and flag_empty:
        flag_empty = False
        index_checker += 1
    if flag_empty:
        return None

    # Check if the array contains zero
    contains_zero: bool = False
    scan_pointer: int = 0
    while scan_pointer < len(array_of_integers):
        current_element: int = array_of_integers[scan_pointer]
        if current_element == 0:
            contains_zero = True
            break
        scan_pointer += 1

    if contains_zero:
        sign_product = 0
    else:
        # Count negative numbers
        neg_counter: int = 0
        traverse_index: int = 0
        while traverse_index < len(array_of_integers):
            probe_element: int = array_of_integers[traverse_index]
            if probe_element < 0:
                neg_counter += 1
            traverse_index += 1

        # Calculate (-1)**neg_counter
        power_base: int = -1
        exponent_result: int = 1
        exponent_counter: int = 0
        while exponent_counter < neg_counter:
            exponent_result *= power_base
            exponent_counter += 1
        sign_product = exponent_result

    # Sum of absolute values
    sum_abs_values: int = 0
    accumulation_index: int = 0
    while accumulation_index < len(array_of_integers):
        magnitude: int = array_of_integers[accumulation_index]
        if magnitude < 0:
            magnitude = -magnitude
        sum_abs_values += magnitude
        accumulation_index += 1

    return sign_product * sum_abs_values