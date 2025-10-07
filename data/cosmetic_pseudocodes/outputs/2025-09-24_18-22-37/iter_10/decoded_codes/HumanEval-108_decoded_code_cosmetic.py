from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(flag_value: int) -> int:
        phase_code: int = 1
        if flag_value < 0:
            flag_value = -flag_value
            phase_code = -1

        digits_collection: List[int] = [int(ch) for ch in str(flag_value)]

        digits_collection[0] *= phase_code  # apply sign to first digit

        accumulator_result: int = 0
        scan_idx: int = 0
        while scan_idx < len(digits_collection):
            accumulator_result += digits_collection[scan_idx]
            scan_idx += 1

        return accumulator_result

    temp_results: List[int] = []
    outer_index: int = 0
    while True:
        if outer_index > len(array_of_integers) - 1:
            break
        current_value = array_of_integers[outer_index]
        digit_sum_result = digits_sum(current_value)
        temp_results.append(digit_sum_result)
        outer_index += 1

    filtered_collection: List[int] = []
    temp_index: int = 0
    while temp_index < len(temp_results):
        candidate_value = temp_results[temp_index]
        if candidate_value > 0:
            filtered_collection.append(candidate_value)
        temp_index += 1

    final_length: int = len(filtered_collection)
    return final_length