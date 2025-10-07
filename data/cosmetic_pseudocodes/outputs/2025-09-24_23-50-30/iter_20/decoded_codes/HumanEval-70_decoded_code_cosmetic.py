from typing import List


def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    output_sequence: List[int] = []
    switch_indicator: bool = False

    while array_of_numbers:
        switch_indicator = not switch_indicator
        sorted_array = sorted(array_of_numbers)
        if switch_indicator:
            chosen_element = sorted_array[0]
        else:
            chosen_element = sorted_array[-1]
        output_sequence.append(chosen_element)
        array_of_numbers.remove(chosen_element)

    return output_sequence