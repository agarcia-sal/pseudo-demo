from typing import Set


def same_chars(strA: str, strB: str) -> bool:
    uniqueCharsA: Set[str] = set()
    uniqueCharsB: Set[str] = set()

    for character in strA:
        uniqueCharsA.add(character)

    iteratorB = 0
    while iteratorB < len(strB):
        uniqueCharsB.add(strB[iteratorB])
        iteratorB += 1

    return not (uniqueCharsA - uniqueCharsB) and not (uniqueCharsB - uniqueCharsA)