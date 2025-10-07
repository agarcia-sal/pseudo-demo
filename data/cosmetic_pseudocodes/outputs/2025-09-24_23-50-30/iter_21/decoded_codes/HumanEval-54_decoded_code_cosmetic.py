from typing import Set


def same_chars(strA: str, strB: str) -> bool:
    collectionA: Set[str] = set()
    collectionB: Set[str] = set()

    for index in range(1, len(strA) + 1):
        collectionA.add(strA[index - 1])

    for pos in range(1, len(strB) + 1):
        collectionB.add(strB[pos - 1])

    return collectionA == collectionB