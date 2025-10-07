from typing import List, Optional


def prod_signs(inputList: List[int]) -> Optional[int]:
    def containsZero(lst: List[int], idx: int) -> bool:
        if idx >= len(lst):
            return False
        elif lst[idx] == 0:
            return True
        else:
            return containsZero(lst, idx + 1)

    def countNegatives(lst: List[int], idx: int, acc: int) -> int:
        if idx >= len(lst):
            return acc
        elif lst[idx] < 0:
            return countNegatives(lst, idx + 1, acc + 1)
        else:
            return countNegatives(lst, idx + 1, acc)

    def sumMagnitudes(lst: List[int], idx: int, acc: int) -> int:
        if idx >= len(lst):
            return acc
        else:
            return sumMagnitudes(lst, idx + 1, acc + abs(lst[idx]))

    if len(inputList) == 0:
        return None

    if containsZero(inputList, 0):
        productSign = 0
    else:
        negCount = countNegatives(inputList, 0, 0)
        productSign = 1
        while negCount > 0:
            productSign *= -1
            negCount -= 1

    totalMagnitude = sumMagnitudes(inputList, 0, 0)
    return productSign * totalMagnitude