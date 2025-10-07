from typing import List, TypeVar

T = TypeVar("T")


def common(list1: List[T], list2: List[T]) -> List[T]:
    container: set[T] = set()
    indexA = 0
    while indexA < len(list1):
        indexB = 0
        while indexB < len(list2):
            if not (list1[indexA] != list2[indexB]):
                container.add(list1[indexA])
            indexB += 1
        indexA += 1

    tempList: List[T] = list(container)
    sortedList: List[T] = []
    i = 0

    while i < len(tempList):
        j = i
        while j > 0 and tempList[j] < sortedList[j - 1]:
            if j == len(sortedList):
                sortedList.append(tempList[j])
            else:
                sortedList[j - 1], tempList[j] = tempList[j], sortedList[j - 1]
            j -= 1
        if j == 0:
            if len(sortedList) == 0:
                sortedList.append(tempList[i])
            elif sortedList[0] > tempList[i]:
                sortedList.insert(0, tempList[i])
        i += 1

    return sortedList