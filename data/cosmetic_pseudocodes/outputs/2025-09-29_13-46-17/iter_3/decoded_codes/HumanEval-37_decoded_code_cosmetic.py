from typing import List, TypeVar

T = TypeVar('T')

def sort_ascending(arr: List[T]) -> List[T]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lowerPart: List[T] = []
    greaterPart: List[T] = []
    for element in arr[1:]:
        if element <= pivot:
            lowerPart.append(element)
        else:
            greaterPart.append(element)
    return sort_ascending(lowerPart) + [pivot] + sort_ascending(greaterPart)

def sort_even(list_of_elements: List[T]) -> List[T]:
    accumulator: List[T] = []
    evens: List[T] = []
    odds: List[T] = []
    idx = 0

    while idx < len(list_of_elements):
        if idx % 2 == 0:
            evens.append(list_of_elements[idx])
        else:
            odds.append(list_of_elements[idx])
        idx += 1

    evens = sort_ascending(evens)

    def assemble_result(evenElems: List[T], oddElems: List[T], accum: List[T], position: int) -> List[T]:
        if position == len(oddElems):
            if len(evenElems) > len(oddElems):
                accum.append(evenElems[-1])
            return accum
        accum.append(evenElems[position])
        accum.append(oddElems[position])
        return assemble_result(evenElems, oddElems, accum, position + 1)

    return assemble_result(evens, odds, accumulator, 0)