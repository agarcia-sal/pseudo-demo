from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    words_array = input_text.split(" ")
    max_freq = 0
    idx = 0

    while idx < len(words_array):
        current_word = words_array[idx]
        current_count = 0
        inner_idx = 0
        while inner_idx < len(words_array):
            if words_array[inner_idx] == current_word:
                current_count += 1
            inner_idx += 1
        if current_word != "":
            if max_freq < current_count:
                max_freq = current_count
        idx += 1

    if max_freq > 0:
        j = 0
        while j < len(words_array):
            candidate = words_array[j]
            count_candidate = 0
            k = 0
            while k < len(words_array):
                if words_array[k] == candidate:
                    count_candidate += 1
                k += 1
            if count_candidate == max_freq:
                freq_map[candidate] = max_freq
            j += 1

    return freq_map