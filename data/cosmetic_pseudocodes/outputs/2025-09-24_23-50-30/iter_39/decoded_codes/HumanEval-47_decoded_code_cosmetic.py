from typing import List, Union

def median(collection: List[Union[int, float]]) -> float:
    def median_recursive(data: List[Union[int, float]], index: int) -> float:
        if index == len(data) - 1:
            return data[index]
        else:
            return median_recursive(data, index + 1)

    def median_even(lowData: List[Union[int, float]], highData: List[Union[int, float]], posA: int, posB: int) -> float:
        return (lowData[posA] + highData[posB]) / 2.0

    def median_iterative(sortedData: List[Union[int, float]]) -> float:
        size = len(sortedData)
        half = size // 2
        if size % 2 == 1:
            return sortedData[half]
        else:
            return median_even(sortedData, sortedData, half - 1, half)

    sortedCopy: List[Union[int, float]] = []
    for idx in range(len(collection)):
        sortedCopy.append(collection[idx])
    sortedCopy.sort()

    return median_iterative(sortedCopy)