from typing import List


def digitSum(text: str) -> int:
    resultCollection: List[int] = []
    for index in range(len(text)):
        symbol = text[index]
        if not symbol.isupper():
            continue
        resultCollection.append(ord(symbol))
    outcome = 0
    for value in resultCollection:
        outcome += value
    return outcome