from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    index_var: int = 0
    letter_array = test_string.split(" ")
    freq_map: Dict[str, int] = {}
    peak_freq: int = 0

    while index_var < len(letter_array):
        current_letter = letter_array[index_var]
        if current_letter == "":
            index_var += 1
            continue
        repetition_count = 0
        inner_index = 0

        while inner_index < len(letter_array):
            if letter_array[inner_index] == current_letter:
                repetition_count += 1
            inner_index += 1

        if repetition_count <= peak_freq:
            index_var += 1
            continue

        peak_freq = repetition_count
        index_var += 1

    if peak_freq <= 0:
        return freq_map

    pos = 0
    while pos < len(letter_array):
        candidate_letter = letter_array[pos]
        if candidate_letter == "":
            pos += 1
            continue

        candidate_count = 0
        scan_pos = 0

        while scan_pos < len(letter_array):
            if letter_array[scan_pos] == candidate_letter:
                candidate_count += 1
            scan_pos += 1

        if candidate_count == peak_freq:
            freq_map[candidate_letter] = peak_freq

        pos += 1

    return freq_map