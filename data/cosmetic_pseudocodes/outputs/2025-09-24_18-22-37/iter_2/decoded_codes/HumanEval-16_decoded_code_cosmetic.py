from typing import Dict

def count_distinct_characters(txt: str) -> int:
    uniqueChars: Dict[str, None] = {}
    for ch in txt:
        c = ch.lower()
        if c not in uniqueChars:
            uniqueChars[c] = None
    return len(uniqueChars)