from typing import List, TypeVar

T = TypeVar('T')

def sort_non_decreasing(array: List[T]) -> None:
    n: int = len(array)
    i: int = 0
    while i < n - 1:
        j: int = 0
        while j < n - i - 1:
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1
        i += 1

def sort_even(list_of_elements: List[T]) -> List[T]:
    alpha: List[T] = []
    beta: List[T] = []
    gamma: int = 0
    while gamma < len(list_of_elements):
        if gamma % 2 == 0:
            alpha.append(list_of_elements[gamma])
        else:
            beta.append(list_of_elements[gamma])
        gamma += 1

    sort_non_decreasing(alpha)

    delta: List[T] = []

    def merge_pairs(idx: int, merged: List[T]) -> List[T]:
        if idx == min(len(alpha), len(beta)):
            return merged
        merged = merged + [alpha[idx], beta[idx]]
        return merge_pairs(idx + 1, merged)

    delta = merge_pairs(0, delta)

    if len(alpha) > len(beta):
        delta.append(alpha[-1])

    return delta