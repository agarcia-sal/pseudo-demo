from collections import Counter
from typing import Dict

def histogram(input_string: str) -> Dict[str, int]:
    list_of_letters = input_string.split()
    if not list_of_letters:
        return {}

    counts = Counter(filter(None, list_of_letters))
    if not counts:
        return {}

    maximum_count = max(counts.values())
    return {letter: maximum_count for letter, count in counts.items() if count == maximum_count}