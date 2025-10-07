from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars_list = test_string.split(" ")
    max_freq = -1

    def find_max(index: int) -> None:
        nonlocal max_freq
        if index == len(chars_list):
            return
        current_char = chars_list[index]
        if current_char != "" and max_freq < chars_list.count(current_char):
            max_freq = chars_list.count(current_char)
        find_max(index + 1)

    find_max(0)

    if max_freq > 0:
        i = 0
        while i < len(chars_list):
            c = chars_list[i]
            if chars_list.count(c) == max_freq:
                freq_map[c] = max_freq
            i += 1

    return freq_map