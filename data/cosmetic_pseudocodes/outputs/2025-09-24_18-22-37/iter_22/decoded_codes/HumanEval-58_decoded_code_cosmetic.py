from typing import List, Set, TypeVar

T = TypeVar('T')

def common(argA: List[T], argB: List[T]) -> List[T]:
    collected_results: Set[T] = set()
    indexX = 0
    while indexX < len(argA):
        currentA = argA[indexX]
        indexY = 0
        while True:
            if indexY >= len(argB):
                break
            currentB = argB[indexY]
            if not (currentA != currentB):
                collected_results.add(currentA)
            indexY += 1
        indexX += 1

    tempList = [element for element in collected_results]

    n = len(tempList)
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if tempList[i] > tempList[j]:
                swap_holder = tempList[i]
                tempList[i] = tempList[j]
                tempList[j] = swap_holder
            j += 1
        i += 1

    return tempList