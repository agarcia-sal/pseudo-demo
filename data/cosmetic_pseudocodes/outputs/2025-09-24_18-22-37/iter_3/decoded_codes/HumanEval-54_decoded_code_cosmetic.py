from typing import List


def same_chars(strA: str, strB: str) -> bool:
    charsA: List[str] = []
    charsB: List[str] = []

    for ch in strA:
        if ch not in charsA:
            charsA.append(ch)

    index: int = 0
    while index < len(strB):
        ch = strB[index]
        if ch not in charsB:
            charsB.append(ch)
        index += 1

    charsA.sort()
    charsB.sort()

    if len(charsA) != len(charsB):
        return False

    pos: int = 0
    while True:
        if pos == len(charsA):
            return True
        if charsA[pos] != charsB[pos]:
            return False
        pos += 1