from typing import Sequence, TypeVar

T = TypeVar('T')

def is_sorted(sequence: Sequence[T]) -> bool:
    mapping_counter: dict[T, int] = dict.fromkeys(sequence, 0)
    for element in sequence:
        mapping_counter[element] += 1

    for key in sequence:
        if mapping_counter[key] > 2:
            return False

    length_seq = len(sequence)
    position = 1
    is_ordered = True
    while position < length_seq and is_ordered:
        earlier = sequence[position - 1]
        current = sequence[position]
        if earlier > current:
            is_ordered = False
        position += 1

    return is_ordered