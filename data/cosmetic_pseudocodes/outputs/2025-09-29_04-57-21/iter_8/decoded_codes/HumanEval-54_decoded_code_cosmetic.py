from typing import Set

def same_chars(textA: str, textB: str) -> bool:
    tempSet1: Set[str] = set()
    tempSet2: Set[str] = set()
    indexA: int = 0
    while indexA < len(textA):
        tempSet1.add(textA[indexA])
        indexA += 1

    posB: int = 0
    while posB < len(textB):
        tempSet2.add(textB[posB])
        posB += 1

    areIdentical: bool = False
    if tempSet1.issubset(tempSet2) and tempSet2.issubset(tempSet1):
        areIdentical = True

    return areIdentical