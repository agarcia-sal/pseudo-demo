from typing import Dict


def histogram(test_string_param: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    letters_array = test_string_param.split(" ")
    peak_frequency = 0
    index_var = 0

    while index_var < len(letters_array):
        current_letter = letters_array[index_var]
        if current_letter == "":
            index_var += 1
            continue
        current_count = 0
        j = 0
        while j < len(letters_array):
            if letters_array[j] == current_letter:
                current_count += 1
            j += 1
        if current_count > peak_frequency:
            peak_frequency = current_count
        index_var += 1

    if peak_frequency <= 0:
        return frequency_map

    index_var = 0
    while index_var < len(letters_array):
        current_letter = letters_array[index_var]
        current_count = 0
        k = 0
        while k < len(letters_array):
            if letters_array[k] == current_letter:
                current_count += 1
            k += 1
        if current_count == peak_frequency:
            frequency_map[current_letter] = peak_frequency
        index_var += 1

    return frequency_map