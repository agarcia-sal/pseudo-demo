from typing import List, Optional, Tuple

def largest_smallest_integers(list_of_numbers: List[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives_collection: List[int] = []
    positives_collection: List[int] = []

    for number in list_of_numbers:
        if number < 0:
            negatives_collection.append(number)
        elif number > 0:
            positives_collection.append(number)

    highest_negative: Optional[int] = None
    lowest_positive: Optional[int] = None

    if negatives_collection:
        highest_negative = negatives_collection[0]
        for val in negatives_collection:
            if val > highest_negative:
                highest_negative = val

    if positives_collection:
        lowest_positive = positives_collection[0]
        for val in positives_collection[1:]:
            if val < lowest_positive:
                lowest_positive = val

    return highest_negative, lowest_positive