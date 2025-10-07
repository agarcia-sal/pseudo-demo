from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')


class Comparable:
    def __lt__(self: T, other: T) -> bool:
        ...
    def __gt__(self: T, other: T) -> bool:
        ...


def monotonic(array_sequence: Sequence[T]) -> bool:
    forward_sorted_flag: bool = True
    backward_sorted_flag: bool = True
    counter_index: int = 1

    while counter_index < len(array_sequence):
        if array_sequence[counter_index - 1] > array_sequence[counter_index]:
            forward_sorted_flag = False

        if array_sequence[counter_index - 1] < array_sequence[counter_index]:
            backward_sorted_flag = False

        if not (forward_sorted_flag or backward_sorted_flag):
            return False

        counter_index += 1

    return True