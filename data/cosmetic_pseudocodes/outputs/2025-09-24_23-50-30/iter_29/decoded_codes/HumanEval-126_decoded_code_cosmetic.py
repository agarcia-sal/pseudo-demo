from typing import Sequence, TypeVar

T = TypeVar('T', bound=object)

def is_sorted(sequence_of_values: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {element: 0 for element in sequence_of_values}

    def accumulate_frequencies(index: int) -> None:
        if index >= len(sequence_of_values):
            return
        current_element = sequence_of_values[index]
        frequency_map[current_element] += 1
        accumulate_frequencies(index + 1)

    accumulate_frequencies(0)

    for element in sequence_of_values:
        if frequency_map[element] > 2:
            return False

    def check_non_decreasing(pos: int) -> bool:
        return (
            pos >= len(sequence_of_values) - 1 or
            (sequence_of_values[pos - 1] <= sequence_of_values[pos] and check_non_decreasing(pos + 1))
        )

    return check_non_decreasing(1)