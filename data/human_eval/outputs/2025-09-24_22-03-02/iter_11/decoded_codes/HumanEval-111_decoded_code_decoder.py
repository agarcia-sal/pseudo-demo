from collections import Counter
from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    list1 = test.split(' ')
    counts = Counter(word for word in list1 if word)
    if not counts:
        return {}
    t = max(counts.values())
    return {word: t for word, count in counts.items() if count == t}