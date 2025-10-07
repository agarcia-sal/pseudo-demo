from typing import Iterable, Optional

def next_smallest(sequence_of_numbers: Iterable[int]) -> Optional[int]:
    distinct_ordered_collection = []
    for element in sequence_of_numbers:
        if element not in distinct_ordered_collection:
            distinct_ordered_collection.append(element)
    auxiliary_sorted_list = sorted(distinct_ordered_collection)
    threshold_count = 2
    if len(auxiliary_sorted_list) < threshold_count:
        return None
    second_smallest_value = auxiliary_sorted_list[1]
    return second_smallest_value