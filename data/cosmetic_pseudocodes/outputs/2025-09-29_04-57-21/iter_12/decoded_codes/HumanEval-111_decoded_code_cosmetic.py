from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    letters_list = test_string.split(" ")
    top_frequency = -1
    idx = 0

    while idx < len(letters_list):
        current_letter = letters_list[idx]
        current_count = 0
        inner_idx = 0

        while inner_idx < len(letters_list):
            if letters_list[inner_idx] == current_letter:
                current_count += 1
            inner_idx += 1

        if current_count > top_frequency and current_letter != "":
            top_frequency = current_count

        idx += 1

    if top_frequency <= 0:
        return frequency_map

    position = 0
    while position < len(letters_list):
        candidate_letter = letters_list[position]
        tally = 0
        scan_pos = 0

        while scan_pos < len(letters_list):
            if letters_list[scan_pos] == candidate_letter:
                tally += 1
            scan_pos += 1

        if tally == top_frequency and candidate_letter != "":
            frequency_map[candidate_letter] = top_frequency

        position += 1

    return frequency_map