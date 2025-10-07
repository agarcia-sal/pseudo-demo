from typing import Sequence, Optional, Tuple


def largest_smallest_integers(sequence_of_values: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives_collection: list[int] = []
    positives_collection: list[int] = []

    cursor: int = 0
    while cursor < len(sequence_of_values):
        candidate = sequence_of_values[cursor]
        if candidate < 0:
            negatives_collection.append(candidate)
        elif candidate > 0:
            positives_collection.append(candidate)
        cursor += 1

    def select_maximum(elements: list[int]) -> Optional[int]:
        if not elements:
            return None
        peak = elements[0]
        for item in elements:
            if item > peak:
                peak = item
        return peak

    def select_minimum(elements: list[int]) -> Optional[int]:
        if not elements:
            return None
        trough = elements[0]
        for cursor2 in range(len(elements)):
            if elements[cursor2] < trough:
                trough = elements[cursor2]
        return trough

    max_neg_value = select_maximum(negatives_collection)
    min_pos_value = select_minimum(positives_collection)

    return max_neg_value, min_pos_value