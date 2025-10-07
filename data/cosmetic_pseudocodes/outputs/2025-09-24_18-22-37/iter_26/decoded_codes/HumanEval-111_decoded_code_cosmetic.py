from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_array = input_text.split(" ")
    max_freq = 0

    idx = 0
    while idx < len(letters_array):
        current_letter = letters_array[idx]
        if current_letter != "":
            letter_count = 0
            inner_idx = 0
            while inner_idx < len(letters_array):
                if letters_array[inner_idx] == current_letter:
                    letter_count += 1
                inner_idx += 1
            if max_freq < letter_count:
                max_freq = letter_count
        idx += 1

    if max_freq > 0:
        j = 0
        while j < len(letters_array):
            letter_to_check = letters_array[j]
            if letter_to_check != "":
                count_tmp = 0
                k = 0
                while k < len(letters_array):
                    if letters_array[k] == letter_to_check:
                        count_tmp += 1
                    k += 1
                if count_tmp == max_freq:
                    freq_map[letter_to_check] = max_freq
            j += 1

    return freq_map