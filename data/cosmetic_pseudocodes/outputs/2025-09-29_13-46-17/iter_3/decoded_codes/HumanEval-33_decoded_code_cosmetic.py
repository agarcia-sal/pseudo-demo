from typing import List


def sort_third(listInput: List[int]) -> List[int]:
    def recursiveInsert(sortedArr: List[int], val: int) -> List[int]:
        if not sortedArr:
            return [val]
        if val < sortedArr[0]:
            return [val] + sortedArr
        return [sortedArr[0]] + recursiveInsert(sortedArr[1:], val)

    def insertionSort(arr: List[int]) -> List[int]:
        if not arr:
            return []
        head = arr[0]
        tailSorted = insertionSort(arr[1:])
        return recursiveInsert(tailSorted, head)

    copyList: List[int] = [element for element in listInput]

    indicesDivByThree: List[int] = []
    collectedVals: List[int] = []

    i: int = 0
    while i < len(copyList):
        if (i % 3) == 0:
            indicesDivByThree.append(i)
            collectedVals.append(copyList[i])
        i += 1

    sortedVals: List[int] = insertionSort(collectedVals)

    def placeValues(indexList: List[int], vals: List[int], targetList: List[int], pos: int) -> None:
        if pos >= len(indexList):
            return
        targetList[indexList[pos]] = vals[pos]
        placeValues(indexList, vals, targetList, pos + 1)

    placeValues(indicesDivByThree, sortedVals, copyList, 0)

    return copyList