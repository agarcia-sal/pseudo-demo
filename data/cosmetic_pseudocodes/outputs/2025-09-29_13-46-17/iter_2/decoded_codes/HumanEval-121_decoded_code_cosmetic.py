from typing import List


def solution(list_of_integers: List[int]) -> int:
    def helper(index: int, acc: int) -> int:
        if index >= len(list_of_integers):
            return acc
        currentValue = list_of_integers[index]
        newAcc = acc
        if (index % 2 == 0) and (currentValue % 2 == 1):
            newAcc += currentValue
        return helper(index + 1, newAcc)

    return helper(0, 0)