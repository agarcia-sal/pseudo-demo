from typing import Sequence

def is_sorted(sequence_of_values: Sequence[int]) -> bool:
    frequency_map: dict[int, int] = {key: 0 for key in sequence_of_values}
    for element in sequence_of_values:
        frequency_map[element] += 1

    duplicate_found = False
    for key in sequence_of_values:
        if frequency_map[key] > 2:
            duplicate_found = True
            break

    if duplicate_found:
        result_flag = False
    else:
        position = 1
        sorted_flag = True
        length = len(sequence_of_values)
        while position < (length - 1) and sorted_flag:
            prev_value = sequence_of_values[position - 1]
            curr_value = sequence_of_values[position]
            if prev_value <= curr_value:
                sorted_flag = sorted_flag and True
            else:
                sorted_flag = False
            position += 1
        result_flag = sorted_flag

    return result_flag