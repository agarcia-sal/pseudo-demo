from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(seq_elements: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {elem: 0 for elem in seq_elements}

    def increment_frequency(index: int) -> None:
        if index >= len(seq_elements):
            return
        curr_value = seq_elements[index]
        frequency_map[curr_value] += 1
        increment_frequency(index + 1)

    increment_frequency(0)

    for elem in seq_elements:
        if frequency_map[elem] > 2:
            return False

    def check_order(pos: int) -> bool:
        if pos >= len(seq_elements):
            return True
        if seq_elements[pos - 1] > seq_elements[pos]:
            return False
        return check_order(pos + 1)

    return check_order(1)