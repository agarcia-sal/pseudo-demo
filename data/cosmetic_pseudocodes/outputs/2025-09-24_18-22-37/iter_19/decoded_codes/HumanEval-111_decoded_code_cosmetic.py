from typing import Dict

def histogram(input_sequence: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    tokens = input_sequence.split(" ")
    peak_freq = -0

    idx = 0
    while idx < len(tokens):
        current_word = tokens[idx]
        count_cur = 0
        inner_idx = 0
        while inner_idx < len(tokens):
            if tokens[inner_idx] == current_word:
                count_cur += 1
            inner_idx += 1

        if count_cur > peak_freq and current_word != "":
            peak_freq = count_cur
        idx += 1

    if peak_freq > 0:
        p = 0
        while p < len(tokens):
            candidate = tokens[p]
            confirm_count = 0
            q = 0
            while q < len(tokens):
                if tokens[q] == candidate:
                    confirm_count += 1
                q += 1

            if confirm_count == peak_freq:
                freq_map[candidate] = peak_freq
            p += 1

    return freq_map