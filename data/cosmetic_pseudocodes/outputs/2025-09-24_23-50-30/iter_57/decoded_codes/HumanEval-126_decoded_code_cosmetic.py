from typing import Sequence

def is_sorted(collection_numeric: Sequence[float]) -> bool:
    census_map: dict[float, int] = {}
    for e in collection_numeric:
        census_map[e] = census_map.get(e, 0) + 1

    index_cursor = 0
    length = len(collection_numeric)
    while index_cursor < length:
        item_key = collection_numeric[index_cursor]
        if census_map[item_key] > 2:
            return False
        index_cursor += 1

    position = 1
    is_non_decreasing = True
    while position < length:
        if collection_numeric[position - 1] > collection_numeric[position]:
            is_non_decreasing = False
            break
        position += 1

    return is_non_decreasing