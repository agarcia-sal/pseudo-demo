from typing import Sequence, Optional

def next_smallest(numbers_collection: Sequence[int]) -> Optional[int]:
    temp_set: set[int] = set()
    for number in numbers_collection:
        if number not in temp_set:
            temp_set.add(number)

    distinct_elements: list[int] = list(temp_set)
    distinct_elements.sort()

    count_unique: int = len(distinct_elements)

    if count_unique < 2:
        return None

    candidate_element: int = distinct_elements[1]
    return candidate_element