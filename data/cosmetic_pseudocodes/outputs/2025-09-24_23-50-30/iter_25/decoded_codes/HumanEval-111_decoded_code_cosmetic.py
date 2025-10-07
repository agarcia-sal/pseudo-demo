from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_list = test_string.split(" ")
    max_frequency = 0

    idx = 0
    while idx < len(letters_list):
        current_letter = letters_list[idx]
        if current_letter != "":
            count_current = letters_list.count(current_letter)
            if count_current > max_frequency:
                max_frequency = count_current
        idx += 1

    if max_frequency > 0:
        j = 0
        while j < len(letters_list):
            candidate = letters_list[j]
            if letters_list.count(candidate) == max_frequency:
                freq_map[candidate] = max_frequency
            j += 1

    return freq_map