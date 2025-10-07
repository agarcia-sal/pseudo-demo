from typing import Sequence, TypeVar

T = TypeVar('T')


def is_sorted(sequence_of_values: Sequence[T]) -> bool:
    map_frequency: dict[T, int] = {item: 0 for item in sequence_of_values}
    pointer: int = 0
    length: int = len(sequence_of_values)
    while pointer < length:
        current_item = sequence_of_values[pointer]
        map_frequency[current_item] += 1
        pointer += 1

    occurrence_okay: bool = True
    for element in sequence_of_values:
        if map_frequency[element] > 2:
            occurrence_okay = False
            break
    if not occurrence_okay:
        return False

    ascending_order: bool = True
    for position in range(1, length):
        prior = sequence_of_values[position - 1]
        current = sequence_of_values[position]
        if prior > current:
            ascending_order = False
            break

    if ascending_order:
        return True
    else:
        return False