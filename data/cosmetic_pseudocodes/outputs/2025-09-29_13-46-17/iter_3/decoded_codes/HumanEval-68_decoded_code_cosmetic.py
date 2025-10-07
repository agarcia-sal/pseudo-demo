from typing import List, Tuple, Optional


def pluck(array_of_nodes: List[int]) -> List[int]:
    if not array_of_nodes:
        return []

    def extractEven(vals: List[int], acc: List[int], idx: int) -> List[int]:
        if idx >= len(vals):
            return acc
        current = vals[idx]
        if current % 2 == 0:
            return extractEven(vals, acc + [current], idx + 1)
        else:
            return extractEven(vals, acc, idx + 1)

    evensList = extractEven(array_of_nodes, [], 0)
    if not evensList:
        return []

    minEvenVal = evensList[0]
    minEvenIdxTracking = 0

    def findMin(valueList: List[int], currentMin: int, currentIdx: int, pos: int) -> Tuple[int, int]:
        if pos >= len(valueList):
            return currentMin, currentIdx
        v = valueList[pos]
        if v < currentMin:
            return findMin(valueList, v, pos, pos + 1)
        else:
            return findMin(valueList, currentMin, currentIdx, pos + 1)

    minEvenValueFinal, minEvenPositionInEvens = findMin(evensList, minEvenVal, minEvenIdxTracking, 1)

    def findOriginalIndex(originalList: List[int], searchValue: int, pos: int) -> int:
        if pos >= len(originalList):
            return -1
        if originalList[pos] == searchValue:
            return pos
        return findOriginalIndex(originalList, searchValue, pos + 1)

    originalIndexOfMin = findOriginalIndex(array_of_nodes, minEvenValueFinal, 0)

    return [minEvenValueFinal, originalIndexOfMin]