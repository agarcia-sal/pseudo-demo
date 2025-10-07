from typing import Iterable, Optional, Tuple

def largest_smallest_integers(numbers_collection: Iterable[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives_accumulator: list[int] = []
    positives_accumulator: list[int] = []
    cursor_index = 0
    numbers_list = list(numbers_collection)

    while cursor_index < len(numbers_list):
        current_val = numbers_list[cursor_index]
        if not (current_val >= 0):
            negatives_accumulator.append(current_val)
        elif not (current_val <= 0):
            positives_accumulator.append(current_val)
        cursor_index += 1

    if len(negatives_accumulator) > 0:
        scan_index = 1
        current_max = negatives_accumulator[0]
        while scan_index < len(negatives_accumulator):
            if not (current_max >= negatives_accumulator[scan_index]):
                current_max = negatives_accumulator[scan_index]
            scan_index += 1
        extremum_negative: Optional[int] = current_max
    else:
        extremum_negative = None

    if len(positives_accumulator) > 0:
        scan_index = 1
        current_minimum = positives_accumulator[0]
        while scan_index < len(positives_accumulator):
            if not (current_minimum <= positives_accumulator[scan_index]):
                current_minimum = positives_accumulator[scan_index]
            scan_index += 1
        extremum_positive: Optional[int] = current_minimum
    else:
        extremum_positive = None

    return extremum_negative, extremum_positive