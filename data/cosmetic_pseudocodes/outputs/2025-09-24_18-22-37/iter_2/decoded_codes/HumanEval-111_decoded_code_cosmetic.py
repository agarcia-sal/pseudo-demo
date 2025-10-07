from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars = test_string.split(" ")
    top_freq = 0

    # Find the highest frequency of any non-empty string in chars
    for index in range(len(chars)):
        current_char = chars[index]
        if current_char != "":
            occurrence_count = 0
            for idx in range(len(chars)):
                if chars[idx] == current_char:
                    occurrence_count += 1
            if occurrence_count > top_freq:
                top_freq = occurrence_count

    # Collect all non-empty strings whose count equals top_freq
    if top_freq > 0:
        for i in range(len(chars)):
            candidate = chars[i]
            if candidate != "":
                c_count = 0
                for j in range(len(chars)):
                    if chars[j] == candidate:
                        c_count += 1
                if c_count == top_freq:
                    freq_map[candidate] = top_freq

    return freq_map