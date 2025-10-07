from typing import List, TypeVar

T = TypeVar('T')  # Generic type variable for list elements

def sort_even(list_of_elements: List[T]) -> List[T]:
    evens: List[T] = []
    odds: List[T] = []
    i: int = len(list_of_elements) - 1

    # Separate elements into evens and odds by index parity, preserving original relative order
    while i >= 0:
        if i % 2 == 0:
            evens.insert(0, list_of_elements[i])
        else:
            odds.insert(0, list_of_elements[i])
        i -= 1

    # Sort evens array using selection sort (in-place)
    j: int = 0
    while j < len(evens) - 1:
        k: int = j + 1
        while k < len(evens):
            if evens[j] > evens[k]:
                evens[j], evens[k] = evens[k], evens[j]
            k += 1
        j += 1

    output: List[T] = []
    max_len: int = max(len(evens), len(odds))

    def interleave(accumulated: List[T], idx: int) -> List[T]:
        if idx >= max_len:
            return accumulated
        if idx < len(evens):
            accumulated.append(evens[idx])
        if idx < len(odds):
            accumulated.append(odds[idx])
        return interleave(accumulated, idx + 1)

    output = interleave([], 0)
    return output