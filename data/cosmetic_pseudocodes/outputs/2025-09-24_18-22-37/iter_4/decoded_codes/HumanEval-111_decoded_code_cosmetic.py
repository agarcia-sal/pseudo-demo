from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    letters_array = test_string.split(" ")
    max_freq = -1
    idx = 0
    while idx < len(letters_array):
        current_letter = letters_array[idx]
        if current_letter != "":
            occurrences = 0
            inner_idx = 0
            while inner_idx < len(letters_array):
                if letters_array[inner_idx] == current_letter:
                    occurrences += 1
                inner_idx += 1
            if occurrences > max_freq:
                max_freq = occurrences
        idx += 1

    if max_freq > 0:
        j = 0
        while j < len(letters_array):
            candidate_letter = letters_array[j]
            if candidate_letter != "":
                count_candidate = 0
                k = 0
                while k < len(letters_array):
                    if letters_array[k] == candidate_letter:
                        count_candidate += 1
                    k += 1
                if count_candidate == max_freq and candidate_letter not in freq_map:
                    freq_map[candidate_letter] = max_freq
            j += 1

    return freq_map