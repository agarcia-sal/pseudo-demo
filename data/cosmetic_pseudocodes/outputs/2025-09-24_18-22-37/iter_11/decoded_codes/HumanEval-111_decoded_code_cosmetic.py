from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_array = test_string.split(' ')
    max_freq = 0

    idx_outer = 0
    while idx_outer < len(letters_array):
        current_letter = letters_array[idx_outer]
        if current_letter != "":
            freq_counter = 0
            idx_inner = 0
            while idx_inner < len(letters_array):
                if letters_array[idx_inner] == current_letter:
                    freq_counter += 1
                idx_inner += 1
            if freq_counter > max_freq:
                max_freq = freq_counter
        idx_outer += 1

    if max_freq > 0:
        idx_outer = 0
        while idx_outer < len(letters_array):
            current_letter = letters_array[idx_outer]
            freq_counter = 0
            idx_inner = 0
            while idx_inner < len(letters_array):
                if letters_array[idx_inner] == current_letter:
                    freq_counter += 1
                idx_inner += 1
            if freq_counter == max_freq:
                freq_map[current_letter] = max_freq
            idx_outer += 1

    return freq_map