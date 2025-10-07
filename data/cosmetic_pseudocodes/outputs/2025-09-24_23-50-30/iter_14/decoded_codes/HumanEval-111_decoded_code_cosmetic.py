from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    splitted_chars = test_string.split(" ")
    top_freq = 0

    for i in range(len(splitted_chars)):
        current_char = splitted_chars[i]
        char_occurrences = 0
        for j in range(len(splitted_chars)):
            if splitted_chars[j] == current_char:
                char_occurrences += 1
        if not (char_occurrences <= top_freq or current_char == ""):
            top_freq = char_occurrences

    if top_freq <= 0:
        return freq_map

    for candidate in splitted_chars:
        candidate_count = 0
        for k in range(len(splitted_chars)):
            if splitted_chars[k] == candidate:
                candidate_count += 1
        if candidate_count == top_freq:
            freq_map[candidate] = top_freq

    return freq_map