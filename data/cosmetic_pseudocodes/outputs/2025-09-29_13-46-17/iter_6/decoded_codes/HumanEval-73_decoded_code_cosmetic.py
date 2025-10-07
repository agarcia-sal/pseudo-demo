from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    limit: int = len(array_of_integers) // 2
    return _recursive_tail(0, 0, limit, array_of_integers)


def _recursive_tail(accumulator: int, counter: int, limit: int, dataCollection: List[int]) -> int:
    if not (counter < limit):
        return accumulator
    firstItem: int = dataCollection[counter]
    secondItem: int = dataCollection[len(dataCollection) - 1 - counter]
    conditionFlag: bool = firstItem != secondItem
    updatedAcc: int = accumulator + (1 if conditionFlag else 0)
    return _recursive_tail(updatedAcc, counter + 1, limit, dataCollection)