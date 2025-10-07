from typing import List, Sequence, TypeVar

T = TypeVar('T')


def sort_even(original_sequence: Sequence[T]) -> List[T]:
    alternate0: List[T] = []
    alternate1: List[T] = []

    position_marker: int = 0
    while position_marker < len(original_sequence):
        alternate0.append(original_sequence[position_marker])
        position_marker += 2

    position_tracker: int = 1
    while position_tracker < len(original_sequence):
        alternate1.append(original_sequence[position_tracker])
        position_tracker += 2

    alternate0.sort()

    reconstructed_sequence: List[T] = []
    iterator0: int = 0
    iterator1: int = 0
    while iterator0 < len(alternate0):
        reconstructed_sequence.append(alternate0[iterator0])
        if iterator1 < len(alternate1):
            reconstructed_sequence.append(alternate1[iterator1])
        iterator0 += 1
        iterator1 += 1

    if len(alternate0) > len(alternate1):
        tail_element = alternate0[-1]
        reconstructed_sequence.append(tail_element)

    return reconstructed_sequence