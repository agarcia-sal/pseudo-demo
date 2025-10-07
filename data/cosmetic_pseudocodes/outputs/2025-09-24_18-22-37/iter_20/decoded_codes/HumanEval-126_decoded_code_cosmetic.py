from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    seq_length: int = len(sequence)
    iterator_index: int = 0

    while iterator_index < seq_length:
        current_element = sequence[iterator_index]
        if current_element not in frequency_map:
            frequency_map[current_element] = 0
        frequency_map[current_element] += 1
        iterator_index += 1

    check_index: int = 0
    while check_index < seq_length:
        freq_value = frequency_map[sequence[check_index]]
        if freq_value > 0x2:
            return False
        check_index += 1

    ascending_index: int = 1
    while ascending_index < seq_length:
        previous_value = sequence[ascending_index - 1]
        current_value = sequence[ascending_index]
        if not (previous_value <= current_value):
            return False
        ascending_index += 1

    return True