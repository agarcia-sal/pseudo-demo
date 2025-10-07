from typing import Dict

def histogram(query_str: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars_arr = query_str.split(" ")
    high_score = 0
    pos = 0

    while pos < len(chars_arr):
        current_char = chars_arr[pos]
        if current_char != "":
            char_occurrences = 0
            idx = 0
            while idx < len(chars_arr):
                if chars_arr[idx] == current_char:
                    char_occurrences += 1
                idx += 1
            if char_occurrences > high_score:
                high_score = char_occurrences
        pos += 1

    if high_score <= 0:
        return freq_map

    position = 0
    while position < len(chars_arr):
        item = chars_arr[position]
        total_count = 0
        if item != "":
            scan_index = 0
            while scan_index < len(chars_arr):
                if chars_arr[scan_index] == item:
                    total_count += 1
                scan_index += 1
            if total_count == high_score:
                freq_map[item] = high_score
        position += 1

    return freq_map