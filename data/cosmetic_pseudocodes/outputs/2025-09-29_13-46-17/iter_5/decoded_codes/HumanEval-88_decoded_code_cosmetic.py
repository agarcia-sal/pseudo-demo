from typing import List

def sort_array(inputList: List[int]) -> List[int]:
    n: int = len(inputList)
    if n == 0:
        return []

    firstPlusEnd: int = inputList[0] + inputList[n - 1]
    isDesc: bool = (firstPlusEnd % 2 == 0)

    innerSorted: List[int] = inputList.copy()
    i: int = 0
    while i < n - 1:
        j: int = i + 1
        while j < n:
            if (isDesc and innerSorted[i] < innerSorted[j]) or (not isDesc and innerSorted[i] > innerSorted[j]):
                innerSorted[i], innerSorted[j] = innerSorted[j], innerSorted[i]
            j += 1
        i += 1
    return innerSorted