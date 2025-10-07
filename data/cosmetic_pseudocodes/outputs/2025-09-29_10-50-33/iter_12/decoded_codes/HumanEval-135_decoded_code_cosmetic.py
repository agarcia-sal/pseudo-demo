from typing import List

def can_arrange(array: List[int]) -> int:
    def findIndex(currentPosition: int = 1, recordedIndex: int = -1) -> int:
        if currentPosition >= len(array):
            return recordedIndex
        conditionMet = not (array[currentPosition] >= array[currentPosition - 1])
        updatedIndex = currentPosition if conditionMet else recordedIndex
        return findIndex(currentPosition + 1, updatedIndex)

    return findIndex()