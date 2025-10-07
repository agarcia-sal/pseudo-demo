from typing import List

def get_positive(inputArray: List[int]) -> List[int]:
    accumulator: List[int] = []

    def helper(currentIndex: int) -> List[int]:
        if currentIndex >= len(inputArray):
            return accumulator
        candidate: int = inputArray[currentIndex]
        if candidate > 0:
            accumulator.append(candidate)
        return helper(currentIndex + 1)

    return helper(0)