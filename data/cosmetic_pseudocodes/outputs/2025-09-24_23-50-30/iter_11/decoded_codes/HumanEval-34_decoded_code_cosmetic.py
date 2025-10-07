from typing import TypeVar, List, Iterable, Dict

T = TypeVar('T', bound=object)  # Generic type variable

def unique(inputCollection: Iterable[T]) -> List[T]:
    tempSet: Dict[T, bool] = {}
    for item in inputCollection:
        tempSet[item] = True
    accumulator: List[T] = list(tempSet.keys())

    def recursiveSort(arr: List[T], start: int, end: int) -> None:
        if start >= end:
            return
        pivotIndex = start
        pivotValue = arr[pivotIndex]
        left = start + 1
        right = end

        while left <= right:
            if arr[left] > pivotValue:
                arr[left], arr[right] = arr[right], arr[left]
                right -= 1
            else:
                left += 1

        arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
        recursiveSort(arr, start, right - 1)
        recursiveSort(arr, right + 1, end)

    recursiveSort(accumulator, 0, len(accumulator) - 1)
    return accumulator