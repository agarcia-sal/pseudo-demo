from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_array = test_string.split(" ")
    max_freq = 0
    idx = 0

    while idx < len(letters_array):
        current_letter = letters_array[idx]
        if current_letter != "":
            count_current = 0
            inner_idx = 0
            while inner_idx < len(letters_array):
                if letters_array[inner_idx] == current_letter:
                    count_current += 1
                inner_idx += 1
            if count_current > max_freq:
                max_freq = count_current
        idx += 1

    if max_freq > 0:
        j = 0
        while j < len(letters_array):
            candidate = letters_array[j]
            if candidate != "":
                occurences = 0
                k = 0
                while k < len(letters_array):
                    if letters_array[k] == candidate:
                        occurences += 1
                    k += 1
                if occurences == max_freq:
                    freq_map[candidate] = max_freq
            j += 1

    return freq_map