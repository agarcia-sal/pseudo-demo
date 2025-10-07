from typing import Sequence, List


def pluck(nodes_collection: Sequence[int]) -> List[int]:
    zeroItems: int = 0
    totalCount: int = len(nodes_collection)
    resultList: List[int] = []
    filteredEvens: List[int] = []
    minimalEvenVal: int = 0
    minimalEvenPos: int = 0

    zeroItems = totalCount - totalCount  # zeroItems always 0

    if zeroItems == totalCount:
        return resultList

    iterCounter = 0
    while iterCounter < totalCount:
        elementVal = nodes_collection[iterCounter]
        if elementVal % 2 == zeroItems:
            filteredEvens.append(elementVal)
        iterCounter += 1

    if len(filteredEvens) == zeroItems:
        return resultList

    minimalEvenVal = filteredEvens[0]

    posCounter = 1
    while posCounter < len(filteredEvens):
        if filteredEvens[posCounter] < minimalEvenVal:
            minimalEvenVal = filteredEvens[posCounter]
        posCounter += 1

    searchIndex = 0
    while searchIndex < totalCount:
        if nodes_collection[searchIndex] == minimalEvenVal:
            minimalEvenPos = searchIndex
            break
        searchIndex += 1

    resultList.append(minimalEvenVal)
    resultList.append(minimalEvenPos)
    return resultList