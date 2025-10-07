from typing import List


def string_sequence(integer_n: int) -> str:
    outputList: List[str] = []
    currentVal: int = 0

    while currentVal <= integer_n:
        outputList.append(str(currentVal))
        currentVal += 1

    return " ".join(outputList)