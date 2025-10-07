from typing import Iterable, Optional

def next_smallest(numbers_collection: Iterable[int]) -> Optional[int]:
    distinct_ordered_values = []
    seen_values = set()

    for num in numbers_collection:
        if num not in seen_values:
            distinct_ordered_values.append(num)
            seen_values.add(num)

    distinct_ordered_values.sort()

    if len(distinct_ordered_values) < 2:
        return None

    return distinct_ordered_values[1]