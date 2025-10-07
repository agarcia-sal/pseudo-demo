from typing import List, Optional, Tuple


def pluck(inputCollection: List[int]) -> List[int]:
    def recursiveFindEven(collection: List[int], currentIdx: int, acc: List[int]) -> List[int]:
        if currentIdx >= len(collection):
            return acc
        currentElement = collection[currentIdx]
        if currentElement % 2 == 0:
            return recursiveFindEven(collection, currentIdx + 1, acc + [currentElement])
        else:
            return recursiveFindEven(collection, currentIdx + 1, acc)

    evensList = recursiveFindEven(inputCollection, 0, [])
    if not evensList:
        return []

    def recursiveMinFinder(lst: List[int], idx: int, minVal: int, minIdx: int) -> List[int]:
        if idx == len(lst):
            return [minVal, minIdx]
        if lst[idx] < minVal:
            return recursiveMinFinder(lst, idx + 1, lst[idx], idx)
        else:
            return recursiveMinFinder(lst, idx + 1, minVal, minIdx)

    resultPair = recursiveMinFinder(evensList, 1, evensList[0], 0)

    def findOrigIndex(collection: List[int], target: int, pos: int) -> int:
        if pos == len(collection):
            return -1
        if collection[pos] == target:
            return pos
        return findOrigIndex(collection, target, pos + 1)

    originalMinIndex = findOrigIndex(inputCollection, resultPair[0], 0)

    return [resultPair[0], originalMinIndex]