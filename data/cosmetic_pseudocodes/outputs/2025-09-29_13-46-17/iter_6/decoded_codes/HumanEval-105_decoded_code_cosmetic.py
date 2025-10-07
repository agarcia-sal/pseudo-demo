from typing import List, Dict, Optional


def by_length(array_of_integers: List[int]) -> List[str]:
    NumMap: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    def descending_sort(inputList: List[int]) -> List[int]:
        if not inputList:
            return inputList
        pivot = inputList[0]
        lessThanPivot: List[int] = []
        greaterOrEqualPivot: List[int] = []
        for idx in range(1, len(inputList)):
            if inputList[idx] >= pivot:
                greaterOrEqualPivot.append(inputList[idx])
            else:
                lessThanPivot.append(inputList[idx])
        return descending_sort(greaterOrEqualPivot) + [pivot] + descending_sort(lessThanPivot)

    sortedList: List[int] = descending_sort(array_of_integers)

    ResultAccumulator: List[str] = []

    def recursiveAppendIndexed(i: int) -> Optional[List[str]]:
        if i < 0:
            return ResultAccumulator
        currentItem = sortedList[i]
        if currentItem in NumMap:
            # Prepend to accumulator to maintain order as per pseudocode
            ResultAccumulator.insert(0, NumMap[currentItem])
        return recursiveAppendIndexed(i - 1)

    return recursiveAppendIndexed(len(sortedList) - 1)  # type: ignore