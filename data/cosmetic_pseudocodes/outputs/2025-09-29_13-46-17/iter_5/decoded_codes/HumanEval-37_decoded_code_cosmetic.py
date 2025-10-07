from typing import List, TypeVar

T = TypeVar('T')


def sort_even(list_of_elements: List[T]) -> List[T]:
    def interleave_lists(a: List[T], b: List[T], acc: List[T], idx: int) -> List[T]:
        if idx == len(a) and idx == len(b):
            return acc
        elif idx < len(a) and idx < len(b):
            return interleave_lists(a, b, acc + [a[idx], b[idx]], idx + 1)
        elif idx < len(a) and idx >= len(b):
            return acc + [a[idx]]
        else:  # idx >= len(a)
            return acc

    evens: List[T] = []
    odds: List[T] = []
    pos = 0
    while pos < len(list_of_elements):
        if pos % 2 == 0:
            evens.append(list_of_elements[pos])
        else:
            odds.append(list_of_elements[pos])
        pos += 1

    sorted_evens = evens[:]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(sorted_evens) - 1):
            if sorted_evens[i] > sorted_evens[i + 1]:
                sorted_evens[i], sorted_evens[i + 1] = sorted_evens[i + 1], sorted_evens[i]
                swapped = True

    return interleave_lists(sorted_evens, odds, [], 0)