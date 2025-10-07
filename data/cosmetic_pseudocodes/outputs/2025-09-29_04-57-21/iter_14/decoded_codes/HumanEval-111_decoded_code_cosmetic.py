from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars = test_string.split(" ")
    top_frequency = 0
    idx = 0

    while idx < len(chars):
        single_char = chars[idx]
        occurrences = 0
        for element in chars:
            if element == single_char:
                occurrences += 1
        if occurrences > top_frequency and single_char != "":
            top_frequency = occurrences
        idx += 1

    if top_frequency > 0:
        pos = 0
        while pos < len(chars):
            test_char = chars[pos]
            count_check = 0
            for item in chars:
                if item == test_char:
                    count_check += 1
            if count_check == top_frequency:
                freq_map[test_char] = top_frequency
            pos += 1

    return freq_map