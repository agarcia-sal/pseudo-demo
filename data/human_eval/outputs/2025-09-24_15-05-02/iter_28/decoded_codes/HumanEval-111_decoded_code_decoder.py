from collections import Counter
from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    words = test_string.split(" ")
    if not words or all(word == "" for word in words):
        return {}
    counts = Counter(filter(None, words))
    if not counts:
        return {}
    max_count = max(counts.values())
    return {word: max_count for word, count in counts.items() if count == max_count}