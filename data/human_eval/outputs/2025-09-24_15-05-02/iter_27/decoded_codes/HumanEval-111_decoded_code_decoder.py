from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    if not isinstance(test, str):
        raise ValueError("Input must be a string.")

    words = test.split(" ")
    if not words:
        return {}

    max_count: int = 0
    # Count occurrences efficiently using a dictionary
    counts: Dict[str, int] = {}
    for word in words:
        if word:
            counts[word] = counts.get(word, 0) + 1
            if counts[word] > max_count:
                max_count = counts[word]

    if max_count == 0:
        return {}

    # Select all words with count equal to max_count
    return {word: count for word, count in counts.items() if count == max_count}