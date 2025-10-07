from typing import Sequence, Tuple, Optional


def largest_smallest_integers(sequence_of_values: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives_collection: list[int] = []
    positives_collection: list[int] = []

    position: int = 0

    while position < len(sequence_of_values):
        current_entry = sequence_of_values[position]
        if current_entry < 0:
            negatives_collection.append(current_entry)
        elif current_entry > 0:
            positives_collection.append(current_entry)
        position += 1

    maximum_negative: Optional[int] = None
    minimum_positive: Optional[int] = None

    if negatives_collection:
        maximum_negative = negatives_collection[0]
        idx: int = 1
        while idx < len(negatives_collection):
            if negatives_collection[idx] > maximum_negative:
                maximum_negative = negatives_collection[idx]
            idx += 1

    if positives_collection:
        minimum_positive = positives_collection[0]
        counter: int = 1
        while counter < len(positives_collection):
            if positives_collection[counter] < minimum_positive:
                minimum_positive = positives_collection[counter]
            counter += 1

    return maximum_negative, minimum_positive