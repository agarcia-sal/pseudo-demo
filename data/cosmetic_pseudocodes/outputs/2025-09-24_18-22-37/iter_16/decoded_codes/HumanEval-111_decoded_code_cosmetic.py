from typing import Dict

def histogram(w_input: str) -> Dict[str, int]:
    counts_map: Dict[str, int] = {}
    letters_array = w_input.split(" ")
    max_occurrences = 0
    idx = 0

    while idx < len(letters_array):
        current_letter = letters_array[idx]
        if current_letter != "":
            current_count = 0
            jdx = 0
            while jdx < len(letters_array):
                if letters_array[jdx] == current_letter:
                    current_count += 1
                jdx += 1
            if current_count > max_occurrences:
                max_occurrences = current_count
        idx += 1

    if max_occurrences > 0:
        step = 0
        while step < len(letters_array):
            candidate = letters_array[step]
            freq_check = 0
            if candidate != "":
                scan = 0
                while scan < len(letters_array):
                    if letters_array[scan] == candidate:
                        freq_check += 1
                    scan += 1
                if freq_check == max_occurrences:
                    counts_map[candidate] = max_occurrences
            step += 1

    return counts_map