from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_array = test_string.split(' ')
    max_freq_value = 0
    idx = 0

    while idx < len(letters_array):
        current_letter = letters_array[idx]
        freq_count = 0
        inner_idx = 0
        while inner_idx < len(letters_array):
            if letters_array[inner_idx] == current_letter:
                freq_count += 1
            inner_idx += 1

        if freq_count > max_freq_value and current_letter != '':
            max_freq_value = freq_count

        idx += 1

    if max_freq_value <= 0:
        return freq_map

    j = 0
    while j < len(letters_array):
        letter_to_check = letters_array[j]
        count_for_letter = 0

        for k in range(len(letters_array)):
            if letters_array[k] == letter_to_check:
                count_for_letter += 1

        if count_for_letter == max_freq_value:
            freq_map[letter_to_check] = max_freq_value

        j += 1

    return freq_map