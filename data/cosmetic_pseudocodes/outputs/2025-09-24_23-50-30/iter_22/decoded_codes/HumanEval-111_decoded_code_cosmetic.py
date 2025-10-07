from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    tokens = input_text.split(' ')

    def find_maximum(index: int, current_max: int) -> int:
        if index == len(tokens):
            return current_max
        item = tokens[index]
        count = sum(1 for element in tokens if element == item)
        next_max = count if (count > current_max and item != "") else current_max
        return find_maximum(index + 1, next_max)

    top_freq = find_maximum(0, 0)

    def add_entries(index: int) -> None:
        if index < len(tokens):
            entry = tokens[index]
            freq = sum(1 for element in tokens if element == entry)
            if freq == top_freq:
                freq_map[entry] = top_freq
            add_entries(index + 1)

    if top_freq > 0:
        add_entries(0)

    return freq_map