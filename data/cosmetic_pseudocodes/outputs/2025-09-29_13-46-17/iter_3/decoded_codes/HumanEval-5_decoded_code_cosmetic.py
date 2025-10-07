from typing import List


def intersperse(numberArray: List[int], delim: int) -> List[int]:
    if not numberArray:
        return []

    def helper(index: int, acc: List[int]) -> List[int]:
        if index == len(numberArray) - 1:
            return acc + [numberArray[index]]
        else:
            return helper(index + 1, acc + [numberArray[index], delim])

    return helper(0, [])