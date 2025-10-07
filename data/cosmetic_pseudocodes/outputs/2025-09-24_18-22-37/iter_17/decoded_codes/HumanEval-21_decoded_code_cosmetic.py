from typing import List

def rescale_to_unit(arr: List[float]) -> List[float]:
    if not arr:
        return []
    lowVal = arr[0]
    idx = 1
    while idx < len(arr):
        if arr[idx] < lowVal:
            lowVal = arr[idx]
        idx += 1
    highVal = arr[0]
    idx = 1
    while idx < len(arr):
        if arr[idx] > highVal:
            highVal = arr[idx]
        idx += 1
    normDenominator = highVal - lowVal
    if normDenominator == 0:
        return [0.0] * len(arr)
    newList: List[float] = []
    idx = 0
    while idx < len(arr):
        adjustedValue = arr[idx] - lowVal
        adjustedValue = adjustedValue * (1 / normDenominator)
        newList.append(adjustedValue)
        idx += 1
    return newList