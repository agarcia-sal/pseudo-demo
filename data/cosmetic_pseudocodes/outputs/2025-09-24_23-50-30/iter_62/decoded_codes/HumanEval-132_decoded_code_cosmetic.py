from typing import List


def is_nested(identifier: str) -> bool:
    temporaryA: List[int] = []
    temporaryB: List[int] = []
    temporaryC: int = 0
    temporaryD: int = 0
    temporaryE: int = len(identifier)
    while temporaryD < temporaryE:
        if identifier[temporaryD] == '[':
            temporaryA.append(temporaryD)
        else:
            temporaryB.append(temporaryD)
        temporaryD += 1
    temporaryB.reverse()
    for temporaryF in temporaryA:
        if temporaryC < len(temporaryB) and temporaryF < temporaryB[temporaryC]:
            temporaryC += 1
    return temporaryC >= 2