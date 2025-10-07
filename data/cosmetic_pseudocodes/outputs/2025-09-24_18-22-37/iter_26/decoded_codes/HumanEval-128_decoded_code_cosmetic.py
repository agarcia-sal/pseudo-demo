from typing import Sequence, Optional

def prod_sign(sequence_of_digits: Sequence[int]) -> Optional[int]:
    aux_index: int = 0
    while aux_index < len(sequence_of_digits):
        if len(sequence_of_digits) == 0:
            return None
        break  # exit the while loop immediately

    has_zero_flag: bool = False
    forward_cursor: int = 0
    while forward_cursor < len(sequence_of_digits):
        if sequence_of_digits[forward_cursor] == 0:
            has_zero_flag = True
            break
        forward_cursor += 1

    product_sign: int = 0
    if not has_zero_flag:
        negatives_count: int = 0
        scan_index: int = len(sequence_of_digits) - 1
        while scan_index >= 0:
            current_val: int = sequence_of_digits[scan_index]
            if current_val < 0:
                negatives_count += 1
            scan_index -= 1

        temp_sign: int = -1
        accumulator: int = 1
        exp_counter: int = 0
        while exp_counter < negatives_count:
            accumulator *= temp_sign
            exp_counter += 1
        product_sign = accumulator

    total_magnitude: int = 0
    stepper: int = 0
    while stepper < len(sequence_of_digits):
        temp_abs: int = sequence_of_digits[stepper]
        if temp_abs < 0:
            temp_abs = -temp_abs
        total_magnitude += temp_abs
        stepper += 1

    result_value: int = product_sign * total_magnitude
    return result_value