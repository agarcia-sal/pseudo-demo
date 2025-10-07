from typing import Sequence, TypeVar

T = TypeVar('T')

def how_many_times(input_sequence: Sequence[T], search_pattern: Sequence[T]) -> int:
    occurrences_found = 0
    limit_upper = len(input_sequence) - len(search_pattern)
    for position in range(limit_upper + 1):
        if input_sequence[position:position + len(search_pattern)] == search_pattern:
            occurrences_found += 1
    return occurrences_found