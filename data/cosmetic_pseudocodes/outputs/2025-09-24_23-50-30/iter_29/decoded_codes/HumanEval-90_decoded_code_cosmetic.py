from typing import Iterable, Optional

def next_smallest(collection_of_numbers: Iterable[int]) -> Optional[int]:
    distinct_ordered: list[int] = []
    for each_element in collection_of_numbers:
        if each_element not in distinct_ordered:
            distinct_ordered.append(each_element)

    distinct_ordered.sort()

    if len(distinct_ordered) >= 2:
        return distinct_ordered[1]
    return None