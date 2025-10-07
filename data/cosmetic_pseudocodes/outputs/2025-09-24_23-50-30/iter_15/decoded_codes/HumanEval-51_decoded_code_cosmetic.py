from typing import List


def remove_vowels(a1: str) -> str:
    b2: List[str] = []
    for c3 in a1:
        d4 = c3.lower()
        if d4 not in {"a", "e", "i", "o", "u"}:
            b2.append(c3)
    e5 = ""
    for f6 in range(len(b2)):
        e5 += b2[f6]
    return e5