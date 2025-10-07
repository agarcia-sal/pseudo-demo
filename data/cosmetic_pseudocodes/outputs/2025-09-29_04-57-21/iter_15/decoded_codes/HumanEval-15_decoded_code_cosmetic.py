from typing import List


def string_sequence(integer_n: int) -> str:
    buildList: List[str] = []
    currentIndex: int = 0
    while currentIndex <= integer_n:
        buildList.append(str(currentIndex))
        currentIndex += 1
    return " ".join(buildList)