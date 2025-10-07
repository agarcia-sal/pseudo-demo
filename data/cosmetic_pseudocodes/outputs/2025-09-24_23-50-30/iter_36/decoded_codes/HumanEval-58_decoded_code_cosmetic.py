from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def accumulateResults(idxA: int, idxB: int, accSet: Set[T]) -> Set[T]:
        if idxA >= len(list1):
            return accSet
        elif idxB >= len(list2):
            return accumulateResults(idxA + 1, 0, accSet)
        else:
            valX = list1[idxA]
            valY = list2[idxB]
            updatedSet = accSet | {valX} if valX == valY else accSet
            return accumulateResults(idxA, idxB + 1, updatedSet)

    finalSet = accumulateResults(0, 0, set())
    outputList: List[T] = []
    for item in finalSet:
        outputList.append(item)

    for i in range(len(outputList) - 1):
        for j in range(i + 1, len(outputList)):
            if outputList[i] > outputList[j]:
                outputList[i], outputList[j] = outputList[j], outputList[i]

    return outputList