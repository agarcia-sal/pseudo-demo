from typing import List

def pairs_sum_to_zero(listOfIntegers: List[int]) -> bool:
    def checkPair(position: int) -> bool:
        if position >= len(listOfIntegers) - 1:
            return False

        def innerCheck(offset: int) -> bool:
            if offset >= len(listOfIntegers):
                return checkPair(position + 1)
            if listOfIntegers[position] + listOfIntegers[offset] == 0:
                return True
            return innerCheck(offset + 1)

        return innerCheck(position + 1)

    return checkPair(0)