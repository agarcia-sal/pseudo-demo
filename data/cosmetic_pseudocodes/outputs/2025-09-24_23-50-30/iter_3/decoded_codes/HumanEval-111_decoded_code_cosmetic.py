from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    letters_array = test_string.split(" ")
    max_freq = 0

    for idx in range(len(letters_array)):
        current_letter = letters_array[idx]
        if current_letter != "":
            occurrence = 0
            for item in letters_array:
                if item == current_letter:
                    occurrence += 1
            if occurrence > max_freq:
                max_freq = occurrence

    if max_freq > 0:
        for pos in range(len(letters_array)):
            letter_check = letters_array[pos]
            count_check = 0
            for element in letters_array:
                if element == letter_check:
                    count_check += 1
            if count_check == max_freq:
                frequency_map[letter_check] = max_freq

    return frequency_map