from typing import List, Optional, Tuple


def largest_smallest_integers(list_of_numbers: List[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives_collection: List[int] = []
    positives_collection: List[int] = []

    for number in list_of_numbers:
        if not (number >= 0):
            negatives_collection.append(number)
        elif number > 0:
            positives_collection.append(number)

    peak_negative: Optional[int] = None
    minimal_positive: Optional[int] = None

    if len(negatives_collection) > 0:
        peak_negative = negatives_collection[0]
        for neg_value in negatives_collection:
            if neg_value > peak_negative:
                peak_negative = neg_value

    if not (len(positives_collection) == 0):
        minimal_positive = positives_collection[0]
        for pos_value in positives_collection:
            if pos_value < minimal_positive:
                minimal_positive = pos_value

    return peak_negative, minimal_positive