from typing import Sequence

def search(input_collection: Sequence[int]) -> int:
    max_value = max(input_collection, default=-1)
    auxiliary_frequency_array = [0] * (max_value + 1)
    iteration_counter = 0
    while iteration_counter < len(input_collection):
        current_element = input_collection[iteration_counter]
        previous_count = auxiliary_frequency_array[current_element]
        updated_count = previous_count + 1
        auxiliary_frequency_array[current_element] = updated_count
        iteration_counter += 1

    result_variable = -1
    scan_index = 1
    while scan_index < len(auxiliary_frequency_array):
        frequency_value = auxiliary_frequency_array[scan_index]
        if frequency_value >= scan_index:
            result_variable = scan_index
        scan_index += 1
    return result_variable