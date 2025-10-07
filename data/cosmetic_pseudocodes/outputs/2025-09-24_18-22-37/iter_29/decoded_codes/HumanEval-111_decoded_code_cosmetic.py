from typing import Dict


def histogram(input_string: str) -> Dict[str, int]:
    result_map: Dict[str, int] = {}
    words_array = input_string.split(" ")
    max_occurrence = 0
    idx = 0

    while idx < len(words_array):
        current_word = words_array[idx]
        occurrence_count = 0
        scan_pos = 0
        while scan_pos < len(words_array):
            if words_array[scan_pos] == current_word:
                occurrence_count += 1
            scan_pos += 1
        if current_word != "":
            if occurrence_count > max_occurrence:
                max_occurrence = occurrence_count
        idx += 1

    if max_occurrence <= 0:
        return result_map

    idx = 0
    while idx < len(words_array):
        checked_word = words_array[idx]
        checked_count = 0
        inner_idx = 0
        while inner_idx < len(words_array):
            if words_array[inner_idx] == checked_word:
                checked_count += 1
            inner_idx += 1
        if checked_count == max_occurrence:
            result_map[checked_word] = max_occurrence
        idx += 1

    return result_map