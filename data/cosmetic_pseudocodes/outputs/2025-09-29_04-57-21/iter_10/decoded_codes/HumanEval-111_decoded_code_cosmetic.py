from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    letters_array = test_string.split(" ")
    peak_frequency = -1

    idx = 0
    while idx < len(letters_array):
        current_char = letters_array[idx]
        if current_char != "":
            count_occurrences = 0
            jdx = 0
            while jdx < len(letters_array):
                if letters_array[jdx] == current_char:
                    count_occurrences += 1
                jdx += 1
            if count_occurrences > peak_frequency:
                peak_frequency = count_occurrences
        idx += 1

    if peak_frequency <= 0:
        return frequency_map

    pos = 0
    while pos < len(letters_array):
        symbol = letters_array[pos]
        if symbol != "":
            total_count = 0
            counter = 0
            while counter < len(letters_array):
                if letters_array[counter] == symbol:
                    total_count += 1
                counter += 1
            if total_count == peak_frequency:
                if symbol not in frequency_map:
                    frequency_map[symbol] = peak_frequency
        pos += 1

    return frequency_map