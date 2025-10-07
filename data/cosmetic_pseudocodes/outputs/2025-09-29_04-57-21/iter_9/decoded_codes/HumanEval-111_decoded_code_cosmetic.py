from typing import Dict


def histogram(test_string: str) -> Dict[str, int]:
    counts_map: Dict[str, int] = {}
    tokens = test_string.split(' ')
    highest_frequency = -1

    index = 0
    while index < len(tokens):
        current_token = tokens[index]
        if current_token != '':
            occurrences = 0
            inner_index = 0
            while inner_index < len(tokens):
                if tokens[inner_index] == current_token:
                    occurrences += 1
                inner_index += 1
            if highest_frequency < occurrences:
                highest_frequency = occurrences
        index += 1

    if highest_frequency > 0:
        idx = 0
        while idx < len(tokens):
            token_at_idx = tokens[idx]
            if token_at_idx != '':
                occur_count = 0
                search_idx = 0
                while search_idx < len(tokens):
                    if tokens[search_idx] == token_at_idx:
                        occur_count += 1
                    search_idx += 1
                if occur_count == highest_frequency:
                    counts_map[token_at_idx] = highest_frequency
            idx += 1

    return counts_map