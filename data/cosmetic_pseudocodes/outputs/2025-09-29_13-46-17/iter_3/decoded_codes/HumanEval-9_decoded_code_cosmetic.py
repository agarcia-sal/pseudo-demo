from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def helper(numbers: List[int], index: int, currentMax: Optional[int], accumulated: List[int]) -> List[int]:
        if index == len(numbers):
            return accumulated

        currentNumber = numbers[index]

        if currentMax is not None and currentNumber <= currentMax:
            newMax = currentMax
        else:
            newMax = currentNumber

        newAccumulated = accumulated + [newMax]

        return helper(numbers, index + 1, newMax, newAccumulated)

    return helper(list_of_numbers, 0, None, [])