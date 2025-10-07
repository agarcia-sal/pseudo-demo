from typing import Dict

def histogram(alpha_sequence: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    tokens = alpha_sequence.split(" ")
    top_frequency = 0

    def update_max(index: int) -> None:
        nonlocal top_frequency
        if index == len(tokens):
            return
        current_token = tokens[index]
        current_count = tokens.count(current_token)
        if current_count > top_frequency and current_token != "":
            top_frequency = current_count
        update_max(index + 1)

    update_max(0)

    if top_frequency > 0:
        # To avoid redundant counts, use a set for unique elements
        seen = set()
        for element in tokens:
            if element not in seen and element != "" and tokens.count(element) == top_frequency:
                freq_map[element] = top_frequency
                seen.add(element)

    return freq_map