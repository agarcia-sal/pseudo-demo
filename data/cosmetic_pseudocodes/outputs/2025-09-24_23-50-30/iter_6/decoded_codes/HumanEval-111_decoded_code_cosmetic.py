from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars: list[str] = []
    idx: int = 0
    max_freq: int = -1

    while idx < len(test_string):
        if test_string[idx:idx+1] == " ":
            chars.append("")
            idx += 1
        else:
            current_char = ""
            while idx < len(test_string) and test_string[idx:idx+1] != " ":
                current_char += test_string[idx:idx+1]
                idx += 1
            chars.append(current_char)
            continue

    position = 0
    while position < len(chars):
        element = chars[position]
        count_check = 0
        for item in chars:
            if item == element:
                count_check += 1
        if count_check > max_freq and element != "":
            max_freq = count_check
        position += 1

    if max_freq <= 0:
        return freq_map

    pointer = 0
    while pointer < len(chars):
        val = chars[pointer]
        tally = 0
        for element in chars:
            if element == val:
                tally += 1
        if tally == max_freq:
            freq_map[val] = max_freq
        pointer += 1

    return freq_map