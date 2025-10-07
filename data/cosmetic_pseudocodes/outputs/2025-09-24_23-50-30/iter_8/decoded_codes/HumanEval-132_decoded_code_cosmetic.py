from typing import List


def is_nested(string: str) -> bool:
    listA: List[int] = []
    listB: List[int] = []
    idx: int = 0

    while idx != len(string):
        if string[idx] == '[':
            listA.append(idx)
        else:
            listB.append(idx)
        idx += 1

    reversedB: List[int] = []
    temp: int = len(listB) - 1
    while temp >= 0:
        reversedB.append(listB[temp])
        temp -= 1

    matchCount: int = 0
    posB: int = 0
    for element in listA:
        if posB < len(reversedB):
            if element < reversedB[posB]:
                matchCount += 1
                posB += 1

    return (matchCount - 1) >= 1