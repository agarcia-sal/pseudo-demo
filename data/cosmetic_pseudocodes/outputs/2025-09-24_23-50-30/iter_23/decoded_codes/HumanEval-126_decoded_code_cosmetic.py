from typing import Sequence, TypeVar

T = TypeVar('T', bound='supports_comparison')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {element: 0 for element in sequence}
    for element in sequence:
        frequency_map[element] += 1

    for key in sequence:
        if frequency_map[key] > 2:
            return False

    for index in range(2, len(sequence)):
        if not (sequence[index - 1] <= sequence[index]):
            return False

    return True