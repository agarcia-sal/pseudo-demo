from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars_list = test_string.split(" ")
    highest_freq = 0

    idx = 0
    while idx < len(chars_list):
        current_char = chars_list[idx]
        if current_char != "":
            count_current = 0
            for elem in chars_list:
                if elem == current_char:
                    count_current += 1
            if count_current > highest_freq:
                highest_freq = count_current
        idx += 1

    if highest_freq > 0:
        for ch in chars_list:
            ch_count = 0
            for i in range(len(chars_list)):
                if chars_list[i] == ch:
                    ch_count += 1
            if ch_count == highest_freq:
                freq_map[ch] = highest_freq

    return freq_map