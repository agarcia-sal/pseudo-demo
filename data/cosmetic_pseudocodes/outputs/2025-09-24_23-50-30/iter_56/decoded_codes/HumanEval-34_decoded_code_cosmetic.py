from typing import List, TypeVar

T = TypeVar('T')

def unique(auxiliaryList: List[T]) -> List[T]:
    intermediateSet = set()
    interimArray: List[T] = []
    for auxiliaryIndex in range(len(auxiliaryList)):
        if auxiliaryList[auxiliaryIndex] not in intermediateSet:
            intermediateSet.add(auxiliaryList[auxiliaryIndex])
    for eachElement in intermediateSet:
        interimArray.append(eachElement)
    sortIndex1 = 0
    while sortIndex1 < len(interimArray) - 1:
        sortIndex2 = 0
        while sortIndex2 < len(interimArray) - 1 - sortIndex1:
            if interimArray[sortIndex2] > interimArray[sortIndex2 + 1]:
                tempHolder: T = interimArray[sortIndex2]
                interimArray[sortIndex2] = interimArray[sortIndex2 + 1]
                interimArray[sortIndex2 + 1] = tempHolder
            sortIndex2 += 1
        sortIndex1 += 1
    return interimArray