from typing import List, Tuple, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    def split_indices(
        idx: int,
        accumulator_even: List[T],
        accumulator_odd: List[T],
    ) -> Tuple[List[T], List[T]]:
        if idx >= len(list_of_elements):
            return accumulator_even, accumulator_odd
        if idx % 2 == 0:
            return split_indices(idx + 1, accumulator_even + [list_of_elements[idx]], accumulator_odd)
        else:
            return split_indices(idx + 1, accumulator_even, accumulator_odd + [list_of_elements[idx]])

    evens, odds = split_indices(0, [], [])
    sorted_evens = evens[:]
    sorted_evens.sort()
    combined: List[T] = []

    def interleave_pairs(i: int) -> None:
        if i >= len(odds):
            return
        combined.append(sorted_evens[i])
        combined.append(odds[i])
        interleave_pairs(i + 1)

    interleave_pairs(0)

    if len(sorted_evens) > len(odds):
        combined.append(sorted_evens[-1])

    return combined