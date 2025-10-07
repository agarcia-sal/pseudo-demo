from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_list = test_string.split(" ")
    top_count = 0
    idx = 0

    while idx < len(letters_list):
        current_char = letters_list[idx]
        if current_char == "":
            idx += 1
            continue

        count_current = 0
        inner_idx = 0
        while inner_idx < len(letters_list):
            if letters_list[inner_idx] == current_char:
                count_current += 1
            inner_idx += 1

        if count_current > top_count:
            top_count = count_current
        idx += 1

    if top_count > 0:
        pos = 0
        while pos < len(letters_list):
            letter_candidate = letters_list[pos]
            frequency = 0
            scan = 0
            while scan < len(letters_list):
                if letters_list[scan] == letter_candidate:
                    frequency += 1
                scan += 1
            if frequency == top_count:
                freq_map[letter_candidate] = top_count
            pos += 1

    return freq_map