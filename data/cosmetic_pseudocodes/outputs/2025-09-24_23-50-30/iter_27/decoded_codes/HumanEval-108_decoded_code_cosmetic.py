from typing import Sequence, List


def count_nums(sequence_of_numbers: Sequence[int]) -> int:
    def digits_sum(numerical_input: int) -> int:
        factor = 1
        if numerical_input < 0:
            numerical_input = -numerical_input
            factor = -1
        digits_arr = list(str(numerical_input))
        # Apply factor to first digit (converted back to int)
        digits_arr[0] = str(int(digits_arr[0]) * factor)
        total_sum = 0
        idx2 = 0
        while idx2 < len(digits_arr):
            total_sum += int(digits_arr[idx2])
            idx2 += 1
        return total_sum

    collected_sums: List[int] = []
    pos_counter = 0
    while pos_counter < len(sequence_of_numbers):
        current_val = sequence_of_numbers[pos_counter]
        computed_sum = digits_sum(current_val)
        collected_sums.append(computed_sum)
        pos_counter += 1

    result_list: List[int] = []
    iterator_idx = 0
    while iterator_idx < len(collected_sums):
        if collected_sums[iterator_idx] > 0:
            result_list.append(collected_sums[iterator_idx])
        iterator_idx += 1

    return len(result_list)