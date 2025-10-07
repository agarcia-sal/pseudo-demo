from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    seg_even: List[T] = []
    seg_odd: List[T] = []
    idx: int = 0
    while idx < len(list_of_elements):
        if (idx % 2) == 0:
            seg_even.append(list_of_elements[idx])
        else:
            seg_odd.append(list_of_elements[idx])
        idx += 1
    segment_sort(seg_even)
    result_collection: List[T] = []
    limit = min(len(seg_even), len(seg_odd))
    for pos in range(limit):
        result_collection.append(seg_even[pos])
        result_collection.append(seg_odd[pos])
    if len(seg_even) > len(seg_odd):
        result_collection.append(seg_even[-1])
    return result_collection

def segment_sort(collection: List[T]) -> None:
    changed = True
    while changed:
        changed = False
        for k in range(1, len(collection)):
            if collection[k - 1] > collection[k]:
                collection[k - 1], collection[k] = collection[k], collection[k - 1]
                changed = True