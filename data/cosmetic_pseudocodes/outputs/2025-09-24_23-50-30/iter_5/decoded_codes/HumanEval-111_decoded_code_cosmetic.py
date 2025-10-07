from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    tokens = [item for item in test_string.split(" ") if item != ""]
    map_counts: Dict[str, int] = {}

    max_freq: int = 0

    def update_max(idx: int) -> int:
        nonlocal max_freq
        if idx == len(tokens):
            return max_freq
        current = tokens[idx]
        current_count = tokens.count(current)
        if current_count > max_freq:
            max_freq = current_count
        return update_max(idx + 1)

    max_freq = update_max(0)

    if max_freq > 0:
        for idx in range(len(tokens)):
            candidate = tokens[idx]
            freq = tokens.count(candidate)
            if freq == max_freq:
                map_counts[candidate] = max_freq

    return map_counts