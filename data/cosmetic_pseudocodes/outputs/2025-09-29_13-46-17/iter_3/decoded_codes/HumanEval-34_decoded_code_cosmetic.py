from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    def toList(setValue: set[T]) -> List[T]:
        iterator = iter(setValue)
        resultList: List[T] = []

        def innerLoop() -> List[T]:
            try:
                resultList.append(next(iterator))
                return innerLoop()
            except StopIteration:
                return resultList

        return innerLoop()

    uniqueSet = set(list_of_elements)
    unsortedList = toList(uniqueSet)

    def insertSorted(accumulatedList: List[T], element: T) -> List[T]:
        if not accumulatedList:
            return [element]
        if element <= accumulatedList[0]:
            return [element] + accumulatedList
        else:
            return [accumulatedList[0]] + insertSorted(accumulatedList[1:], element)

    def sortList(inputList: List[T]) -> List[T]:
        if not inputList:
            return []
        return insertSorted(sortList(inputList[1:]), inputList[0])

    return sortList(unsortedList)