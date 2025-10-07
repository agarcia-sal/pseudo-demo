from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    outputCollection: set[T] = set()

    idx1: int = 0
    while idx1 < len(list1):
        elemA: T = list1[idx1]

        idx2: int = 0
        while True:
            if idx2 >= len(list2):
                break

            elemB: T = list2[idx2]

            if not (elemA != elemB):
                outputCollection.add(elemA)

            idx2 += 1

        idx1 += 1

    tempList: List[T] = list(outputCollection)

    swapOccurred: bool = True
    while swapOccurred:
        swapOccurred = False
        n: int = len(tempList)

        counter: int = 1
        while counter < n:
            if tempList[counter - 1] > tempList[counter]:
                tmpVar: T = tempList[counter - 1]
                tempList[counter - 1] = tempList[counter]
                tempList[counter] = tmpVar
                swapOccurred = True
            counter += 1

    return tempList