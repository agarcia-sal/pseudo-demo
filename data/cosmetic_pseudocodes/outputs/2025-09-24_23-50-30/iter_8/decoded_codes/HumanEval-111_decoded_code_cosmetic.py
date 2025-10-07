from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    split_letters = test_string.split(" ")
    peak_value = 0
    frequency_map: Dict[str, int] = {}

    index = 0
    while index < len(split_letters):
        current_symbol = split_letters[index]
        occurrences = 0
        inner_idx = 0
        while inner_idx < len(split_letters):
            if split_letters[inner_idx] == current_symbol:
                occurrences += 1
            inner_idx += 1
        if current_symbol != "" and occurrences > peak_value:
            peak_value = occurrences
        index += 1

    if peak_value > 0:
        for position in range(len(split_letters)):
            candidate = split_letters[position]
            count_candidate = 0
            counter = 0
            while counter < len(split_letters):
                if split_letters[counter] == candidate:
                    count_candidate += 1
                counter += 1
            if count_candidate == peak_value:
                frequency_map[candidate] = peak_value

    return frequency_map