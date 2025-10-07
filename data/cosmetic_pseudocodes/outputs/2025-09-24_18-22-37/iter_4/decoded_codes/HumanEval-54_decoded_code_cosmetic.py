from typing import Set


def same_chars(strA: str, strB: str) -> bool:
    setA: Set[str] = set()
    setB: Set[str] = set()
    indexA: int = 0
    indexB: int = 0

    while indexA < len(strA):
        setA.add(strA[indexA])
        indexA += 1

    while indexB < len(strB):
        setB.add(strB[indexB])
        indexB += 1

    return setA == setB