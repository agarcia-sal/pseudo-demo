from typing import Dict


def histogram(input_str: str) -> Dict[str, int]:
    counts_map: Dict[str, int] = {}
    tokens = input_str.split(" ")
    max_freq: int = 0

    idx: int = 0
    while idx < len(tokens):
        current_token: str = tokens[idx]
        if current_token != "":
            current_count: int = 0
            j: int = 0
            while j < len(tokens):
                if tokens[j] == current_token:
                    current_count += 1
                j += 1
            if max_freq < current_count:
                max_freq = current_count
        idx += 1

    if max_freq > 0:
        idx = 0
        while idx < len(tokens):
            word: str = tokens[idx]
            count_for_word: int = 0
            if word != "":
                j = 0
                while j < len(tokens):
                    if tokens[j] == word:
                        count_for_word += 1
                    j += 1
                if count_for_word == max_freq:
                    counts_map[word] = max_freq
            idx += 1

    return counts_map