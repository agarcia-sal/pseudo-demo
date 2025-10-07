from typing import Iterable, List


def count_nums(input_collection: Iterable[int]) -> int:
    def digits_sum(parameter_x: int) -> int:
        factor_sign = 1
        if parameter_x < 0:
            parameter_x = -parameter_x
            factor_sign = -1
        digit_chars = str(parameter_x)
        digits_array: List[int] = []
        index_z = 0
        while index_z < len(digit_chars):
            digits_array.append(int(digit_chars[index_z]))
            index_z += 1
        # Apply sign to the first digit
        digits_array[0] = digits_array[0] * factor_sign
        total_sum = 0
        idx_y = 0
        while idx_y < len(digits_array):
            total_sum += digits_array[idx_y]
            idx_y += 1
        return total_sum

    results_intermediate: List[int] = []
    iter_index = 0
    input_list = list(input_collection)  # ensure index-accessible
    while iter_index < len(input_list):
        current_val = input_list[iter_index]
        computed_sum = digits_sum(current_val)
        results_intermediate.append(computed_sum)
        iter_index += 1

    final_values: List[int] = []
    scan_index = 0
    while scan_index < len(results_intermediate):
        element_v = results_intermediate[scan_index]
        if not (element_v <= 0):
            final_values.append(element_v)
        scan_index += 1

    return len(final_values)