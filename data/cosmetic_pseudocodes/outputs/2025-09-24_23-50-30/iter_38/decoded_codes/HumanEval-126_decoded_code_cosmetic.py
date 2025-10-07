from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __le__(self, other: object) -> bool: ...
    # This is a protocol-like base for type hinting objects supporting <=

def is_sorted(sequence_of_values: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {}
    for key_element in sequence_of_values:
        frequency_map[key_element] = 0
    for element_value in sequence_of_values:
        frequency_map[element_value] += 1
    for index_var in range(len(sequence_of_values)):
        if frequency_map[sequence_of_values[index_var]] > 2:
            return False
    for idx_var in range(1, len(sequence_of_values)):
        if not (sequence_of_values[idx_var - 1] <= sequence_of_values[idx_var]):
            return False
    return True