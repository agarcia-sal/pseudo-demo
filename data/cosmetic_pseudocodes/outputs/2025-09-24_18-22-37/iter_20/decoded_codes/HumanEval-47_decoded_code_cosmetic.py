from typing import Sequence, Union

def median(sequence_of_values: Sequence[Union[int, float]]) -> float:
    ordered_sequence: list[Union[int, float]] = []

    # Copy input values preserving order
    for position in range(len(sequence_of_values)):
        ordered_sequence.insert(position, sequence_of_values[position])

    # Insertion sort on the copied list
    sorting_index: int = 1
    while sorting_index < len(ordered_sequence):
        current_value = ordered_sequence[sorting_index]
        scan_index = sorting_index - 1

        while scan_index >= 0 and ordered_sequence[scan_index] > current_value:
            ordered_sequence[scan_index + 1] = ordered_sequence[scan_index]
            scan_index -= 1

        ordered_sequence[scan_index + 1] = current_value
        sorting_index += 1

    total_items: int = len(ordered_sequence)

    if total_items % 2 != 0:
        half_point = (total_items - 1) // 2
        return float(ordered_sequence[half_point])

    half_point = total_items // 2
    first_mid_element = ordered_sequence[half_point - 1]
    second_mid_element = ordered_sequence[half_point]
    computed_median = (first_mid_element + second_mid_element) * 0.5

    return float(computed_median)