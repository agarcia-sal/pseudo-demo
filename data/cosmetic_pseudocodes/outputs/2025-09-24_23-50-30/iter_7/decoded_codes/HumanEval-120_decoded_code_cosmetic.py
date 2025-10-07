from typing import List


def maximum(arr: List[int], num: int) -> List[int]:
    if num <= 0:
        return []

    def quicksort(L: List[int]) -> List[int]:
        if len(L) <= 1:
            return L
        pivot = L[0]
        less = quicksort([x for x in L if x < pivot])
        equal = [y for y in L if y == pivot]
        greater = quicksort([z for z in L if z > pivot])
        return less + equal + greater

    sorted_arr = quicksort(arr)
    start_idx = len(sorted_arr) - num
    collected: List[int] = []
    for i in range(start_idx, len(sorted_arr)):
        collected.append(sorted_arr[i])
    return collected