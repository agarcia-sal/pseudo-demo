from typing import List, TypeVar

T = TypeVar('T')

def bubble_sort_non_decreasing(arr: List[T]) -> None:
    n: int = len(arr)
    i: int = 0
    while i < n - 1:
        j: int = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1

def sort_even(list_of_elements: List[T]) -> List[T]:
    listA: List[T] = []
    listB: List[T] = []
    resultList: List[T] = []
    idx: int = 0
    length: int = len(list_of_elements)
    while idx < length:
        if (idx % 2) == 0:
            listA.append(list_of_elements[idx])
        else:
            listB.append(list_of_elements[idx])
        idx += 1

    bubble_sort_non_decreasing(listA)

    ptrA: int = 0
    ptrB: int = 0
    lenA: int = len(listA)
    lenB: int = len(listB)
    while ptrA < lenA or ptrB < lenB:
        if ptrA < lenA:
            resultList.append(listA[ptrA])
            ptrA += 1
        if ptrB < lenB:
            resultList.append(listB[ptrB])
            ptrB += 1

    return resultList