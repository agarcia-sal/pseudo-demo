from typing import Sequence, Optional, TypeVar, List

T = TypeVar('T')


def next_smallest(ranged_values: Sequence[T]) -> Optional[T]:
    filtered_values: List[T] = []
    index = 0

    while index < len(ranged_values):
        current = ranged_values[index]
        if current not in filtered_values:
            filtered_values.append(current)
        index += 1

    # Bubble sort to sort filtered_values in ascending order
    swapped = True
    filtered_values_sorted = filtered_values[:]
    while swapped:
        swapped = False
        pos = 0
        while pos < len(filtered_values_sorted) - 1:
            if filtered_values_sorted[pos] > filtered_values_sorted[pos + 1]:
                filtered_values_sorted[pos], filtered_values_sorted[pos + 1] = (
                    filtered_values_sorted[pos + 1],
                    filtered_values_sorted[pos],
                )
                swapped = True
            pos += 1

    if len(filtered_values_sorted) >= 2:
        return filtered_values_sorted[1]

    return None