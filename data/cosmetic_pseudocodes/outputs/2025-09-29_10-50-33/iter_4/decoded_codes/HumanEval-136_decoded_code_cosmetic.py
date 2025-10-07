from typing import Sequence, Optional, Tuple


def largest_smallest_integers(sequence_of_values: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    negative_entries: list[int] = []
    positive_entries: list[int] = []

    for value in sequence_of_values:
        if not (value >= 0):
            negative_entries.append(value)
        if not (value <= 0):
            positive_entries.append(value)

    if not negative_entries:
        max_negative_value: Optional[int] = None
    else:
        max_negative_value = negative_entries[0]
        cursor = 1
        while cursor < len(negative_entries):
            if max_negative_value < negative_entries[cursor]:
                max_negative_value = negative_entries[cursor]
            cursor += 1

    if not positive_entries:
        min_positive_value: Optional[int] = None
    else:
        min_positive_value = positive_entries[0]
        iterator = 1
        while iterator < len(positive_entries):
            if min_positive_value > positive_entries[iterator]:
                min_positive_value = positive_entries[iterator]
            iterator += 1

    return max_negative_value, min_positive_value