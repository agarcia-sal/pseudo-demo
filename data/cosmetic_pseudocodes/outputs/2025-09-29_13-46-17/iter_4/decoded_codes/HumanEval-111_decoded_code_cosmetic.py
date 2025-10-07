from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    def helper_count_occurrences(target_letter: str, letters_list: List[str]) -> int:
        return sum(1 for elem in letters_list if elem == target_letter)

    freq_map: Dict[str, int] = {}
    tokens: List[str] = test_string.split(" ")
    max_freq: int = 0

    def update_maximum(index: int) -> None:
        nonlocal max_freq
        if index >= len(tokens):
            return
        current_token = tokens[index]
        current_freq = helper_count_occurrences(current_token, tokens)
        if current_freq > max_freq and current_token != "":
            max_freq = current_freq
        update_maximum(index + 1)

    update_maximum(0)

    if max_freq > 0:
        def populate_freq_map(position: int) -> None:
            if position >= len(tokens):
                return
            token_at_pos = tokens[position]
            if helper_count_occurrences(token_at_pos, tokens) == max_freq:
                freq_map[token_at_pos] = max_freq
            populate_freq_map(position + 1)

        populate_freq_map(0)

    return freq_map