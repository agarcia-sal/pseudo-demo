from collections import deque
from typing import Dict, List

def count_occurrences(target: str, collection: List[str]) -> int:
    count_tracker: int = 0
    for element in collection:
        if element == target:
            count_tracker += 1
    return count_tracker

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    chars: deque[str] = deque(test_string.split(" "))
    top_count: int = -1

    for _ in range(len(chars)):
        current_char: str = chars.popleft()
        chars.append(current_char)
        if current_char != "" and (count_occurrences(current_char, list(chars)) > top_count):
            top_count = count_occurrences(current_char, list(chars))

    if top_count > 0:
        for probe_char in chars:
            if count_occurrences(probe_char, list(chars)) == top_count:
                freq_map[probe_char] = top_count

    return freq_map