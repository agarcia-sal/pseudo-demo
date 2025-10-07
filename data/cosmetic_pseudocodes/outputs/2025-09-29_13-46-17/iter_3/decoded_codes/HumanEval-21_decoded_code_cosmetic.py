from typing import List


def rescale_to_unit(listOfNums: List[float]) -> List[float]:
    minVal: float = float('inf')
    maxVal: float = float('-inf')
    for number in listOfNums:
        if number < minVal:
            minVal = number
        if number > maxVal:
            maxVal = number

    def normalizeAt(index: int) -> List[float]:
        if index >= len(listOfNums):
            return []
        currentNum = listOfNums[index]
        # Avoid division by zero if all numbers are equal
        scaledValue = (currentNum - minVal) / (maxVal - minVal) if maxVal != minVal else 0.0
        return [scaledValue] + normalizeAt(index + 1)

    return normalizeAt(0)