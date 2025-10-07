from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    words = test.split(' ')
    max_count = 0
    # Find the maximum frequency among non-empty words
    for word in words:
        if word and words.count(word) > max_count:
            max_count = words.count(word)
    result: Dict[str, int] = {}
    if max_count > 0:
        for word in words:
            if words.count(word) == max_count:
                result[word] = max_count
    return result