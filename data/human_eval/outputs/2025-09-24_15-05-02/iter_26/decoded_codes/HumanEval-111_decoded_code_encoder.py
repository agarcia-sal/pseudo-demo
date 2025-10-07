from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    if not test_string:
        return {}

    words = test_string.split(' ')
    counts: Dict[str, int] = {}
    max_count = 0

    for word in words:
        if word:
            counts[word] = counts.get(word, 0) + 1
            if counts[word] > max_count:
                max_count = counts[word]

    if max_count == 0:
        return {}
    return {word: count for word, count in counts.items() if count == max_count}