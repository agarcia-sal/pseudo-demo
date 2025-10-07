from typing import Dict


def histogram(input_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_array = input_string.split(' ')
    max_frequency = 0

    idx = 0
    while idx < len(letters_array):
        current_letter = letters_array[idx]
        if current_letter != "":
            count_letter = 0
            j = 0
            while j < len(letters_array):
                if letters_array[j] == current_letter:
                    count_letter += 1
                j += 1
            if count_letter > max_frequency:
                max_frequency = count_letter
        idx += 1

    if max_frequency > 0:
        idx = 0
        while idx < len(letters_array):
            current_letter = letters_array[idx]
            if current_letter != "":
                count_letter = 0
                k = 0
                while k < len(letters_array):
                    if letters_array[k] == current_letter:
                        count_letter += 1
                    k += 1
                if count_letter == max_frequency:
                    freq_map[current_letter] = max_frequency
            idx += 1

    return freq_map