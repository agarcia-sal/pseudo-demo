from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    charsInZero: Set[str] = set()
    charsInOne: Set[str] = set()
    indexA: int = 0

    while indexA < len(string_zero):
        charsInZero.add(string_zero[indexA])
        indexA += 1

    indexB: int = 0
    while indexB < len(string_one):
        charsInOne.add(string_one[indexB])
        indexB += 1

    if charsInZero != charsInOne:
        return False
    return True