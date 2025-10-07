from typing import Sequence

def count_nums(sequence_of_values: Sequence[int]) -> int:
    def digits_sum(num_param: int) -> int:
        polarity_factor = 1
        if num_param < 0:
            num_param = -num_param
            polarity_factor = -1

        digits_str = str(num_param)
        digit_chars_list = [int(ch) for ch in digits_str]
        digit_chars_list[0] *= polarity_factor

        total_sum = sum(digit_chars_list)
        return total_sum

    results_accumulator: list[int] = []
    iterator_idx = 0
    while iterator_idx < len(sequence_of_values):
        current_elem = sequence_of_values[iterator_idx]
        computed_sum = digits_sum(current_elem)
        results_accumulator.append(computed_sum)
        iterator_idx += 1

    positive_sums: list[int] = []
    for entry_index in range(len(results_accumulator)):
        current_entry = results_accumulator[entry_index]
        if not (current_entry <= 0):
            positive_sums.append(current_entry)

    return len(positive_sums)