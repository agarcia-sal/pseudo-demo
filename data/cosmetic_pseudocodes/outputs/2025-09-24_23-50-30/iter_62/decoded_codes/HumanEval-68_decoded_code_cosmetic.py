from typing import List, Optional, Union


def pluck(collection: List[int]) -> List[int]:
    def recursiveCheck(idx: int) -> Optional[List[int]]:
        if idx == len(collection):
            return []
        else:
            return None

    checkResult = recursiveCheck(0)
    if checkResult is not None:
        return checkResult

    def gatherEvens(pos: int, acc: List[int]) -> List[int]:
        if pos == len(collection):
            return acc
        currentElement = collection[pos]
        updatedAcc = acc + [currentElement] if currentElement % 2 == 0 else acc
        return gatherEvens(pos + 1, updatedAcc)

    evensList = gatherEvens(0, [])

    def checkEvens(arr: List[int]) -> Optional[List[int]]:
        if len(arr) == 0:
            return []
        else:
            return None

    evensCheck = checkEvens(evensList)
    if evensCheck is not None:
        return evensCheck

    def findMinAndIndex(lst: List[int], idx: int, currentMin: int, currentIndex: int) -> List[int]:
        if idx == len(lst):
            return [currentMin, currentIndex]
        element = lst[idx]
        if element < currentMin:
            return findMinAndIndex(lst, idx + 1, element, idx)
        else:
            return findMinAndIndex(lst, idx + 1, currentMin, currentIndex)

    initialMin = evensList[0]
    resultPair = findMinAndIndex(evensList, 1, initialMin, 0)

    def locateIndex(collection: List[int], value: int, pos: int) -> int:
        if pos == len(collection):
            return -1
        if collection[pos] == value:
            return pos
        return locateIndex(collection, value, pos + 1)

    minVal = resultPair[0]
    indexInOriginal = locateIndex(collection, minVal, 0)

    return [minVal, indexInOriginal]