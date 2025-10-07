from typing import List, Union

def median(elementsList: List[Union[int, float]]) -> float:
    def medianHelper(arrayData: List[Union[int, float]], dataSize: int) -> float:
        if dataSize % 2 != 0:
            return float(arrayData[(dataSize - 1) // 2])
        return (arrayData[(dataSize // 2) - 1] + arrayData[dataSize // 2]) * 0.5

    sortedArray: List[Union[int, float]] = []
    for idx in range(len(elementsList)):
        sortedArray.append(elementsList[idx])
    sortedArray.sort()

    finalSize = len(sortedArray)
    return medianHelper(sortedArray, finalSize)