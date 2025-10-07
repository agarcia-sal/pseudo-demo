from typing import List, Optional


def next_smallest(array_of_numbers: List[int]) -> Optional[int]:
    distinct_seq = sorted(set(array_of_numbers))
    size_count = len(distinct_seq)

    if size_count < 2:
        return None

    second_element = distinct_seq[1]
    return second_element