from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    words_array = test_string.split(" ")
    max_freq = 0
    idx = 0
    while idx < len(words_array):
        current_word = words_array[idx]
        word_count = 0
        count_idx = 0
        while count_idx < len(words_array):
            if words_array[count_idx] == current_word:
                word_count += 1
            count_idx += 1
        if current_word != "":
            if word_count > max_freq:
                max_freq = word_count
        idx += 1

    if max_freq <= 0:
        return freq_map

    i = 0
    while i < len(words_array):
        candidate = words_array[i]
        candidate_count = 0
        j = 0
        while j < len(words_array):
            if words_array[j] == candidate:
                candidate_count += 1
            j += 1
        if candidate_count == max_freq:
            freq_map[candidate] = max_freq
        i += 1

    return freq_map