from typing import List, Optional, Tuple

def largest_smallest_integers(list_of_numbers: List[int]) -> Tuple[Optional[int], Optional[int]]:
    list_of_negative_numbers = [x for x in list_of_numbers if x < 0]
    list_of_positive_numbers = [x for x in list_of_numbers if x > 0]
    largest_negative = max(list_of_negative_numbers) if list_of_negative_numbers else None
    smallest_positive = min(list_of_positive_numbers) if list_of_positive_numbers else None
    return (largest_negative, smallest_positive)