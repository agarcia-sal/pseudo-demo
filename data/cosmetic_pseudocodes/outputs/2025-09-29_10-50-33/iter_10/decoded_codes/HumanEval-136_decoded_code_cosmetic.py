from typing import List, Optional, Tuple

def largest_smallest_integers(list_of_numbers: List[int]) -> Tuple[Optional[int], Optional[int]]:
    idx_counter: int = 0
    negative_collection: List[int] = []
    while idx_counter < len(list_of_numbers):
        if list_of_numbers[idx_counter] < 0:
            negative_collection.append(list_of_numbers[idx_counter])
        idx_counter += 1

    position_index: int = 0
    positive_collection: List[int] = []
    while position_index < len(list_of_numbers):
        if list_of_numbers[position_index] > 0:
            positive_collection.append(list_of_numbers[position_index])
        position_index += 1

    largest_negative: Optional[int] = max(negative_collection) if negative_collection else None
    smallest_positive: Optional[int] = min(positive_collection) if positive_collection else None

    return largest_negative, smallest_positive