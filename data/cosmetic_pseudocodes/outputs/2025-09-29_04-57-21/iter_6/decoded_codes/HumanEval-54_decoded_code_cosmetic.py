from typing import Set

def same_chars(strA: str, strB: str) -> bool:
    charsA: Set[str] = set()
    for ch in strA:
        charsA.add(ch)
    charsB: Set[str] = set()
    for ch in strB:
        charsB.add(ch)
    return charsA == charsB