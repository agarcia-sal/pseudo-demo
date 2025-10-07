from typing import List, Optional, Tuple


def largest_smallest_integers(numbers_collection: List[int]) -> Tuple[Optional[int], Optional[int]]:
    negatives_collection: List[int] = []
    positives_collection: List[int] = []

    for element_check in numbers_collection:
        if element_check < 0:
            negatives_collection.append(element_check)
        elif element_check > 0:
            positives_collection.append(element_check)

    def find_maximum(sequence_list: List[int], current_pos: int, current_maximum: int) -> int:
        if current_pos == len(sequence_list):
            return current_maximum
        item_at_pos = sequence_list[current_pos]
        update_maximum = item_at_pos if item_at_pos > current_maximum else current_maximum
        return find_maximum(sequence_list, current_pos + 1, update_maximum)

    def find_minimum(sequence_list: List[int], current_pos: int, current_minimum: int) -> int:
        if current_pos == len(sequence_list):
            return current_minimum
        item_at_pos = sequence_list[current_pos]
        update_minimum = item_at_pos if item_at_pos < current_minimum else current_minimum
        return find_minimum(sequence_list, current_pos + 1, update_minimum)

    largest_negative_value: Optional[int]
    smallest_positive_value: Optional[int]

    if len(negatives_collection) == 0:
        largest_negative_value = None
    else:
        largest_negative_value = find_maximum(negatives_collection, 0, negatives_collection[0])

    if len(positives_collection) == 0:
        smallest_positive_value = None
    else:
        smallest_positive_value = find_minimum(positives_collection, 0, positives_collection[0])

    return largest_negative_value, smallest_positive_value