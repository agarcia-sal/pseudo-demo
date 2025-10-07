from typing import List


def add(listOfInts: List[int]) -> int:
    def sumEvenAtOddIndices(index: int, accumulator: int) -> int:
        if index >= len(listOfInts):
            return accumulator
        if listOfInts[index] % 2 == 0:
            accumulator += listOfInts[index]
        return sumEvenAtOddIndices(index + 2, accumulator)

    return sumEvenAtOddIndices(1, 0)