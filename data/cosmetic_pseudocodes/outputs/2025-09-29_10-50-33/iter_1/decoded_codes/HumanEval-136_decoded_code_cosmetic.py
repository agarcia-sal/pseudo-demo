from typing import List, Optional, Tuple


def largest_smallest_integers(list_of_numbers: List[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives: List[int] = []
    positives: List[int] = []

    for number in list_of_numbers:
        if number < 0:
            negatives.append(number)
        elif number > 0:
            positives.append(number)

    if negatives:
        largest_negative: int = negatives[0]
        for n in negatives:
            if n > largest_negative:
                largest_negative = n
    else:
        largest_negative = None

    if positives:
        smallest_positive: int = positives[0]
        for p in positives:
            if p < smallest_positive:
                smallest_positive = p
    else:
        smallest_positive = None

    return largest_negative, smallest_positive