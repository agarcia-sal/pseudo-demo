from typing import Sequence


def is_sorted(collection_numbers: Sequence[int]) -> bool:
    map_quantity: dict[int, int] = {}
    for element in collection_numbers:
        map_quantity[element] = map_quantity.get(element, 0) + 1

    def has_excess_occurrence(index: int) -> bool:
        if index >= len(collection_numbers):
            return False
        key = collection_numbers[index]
        if map_quantity[key] > 2:
            return True
        return has_excess_occurrence(index + 1)

    if has_excess_occurrence(0):
        return False

    def check_non_decreasing(position: int) -> bool:
        if position >= len(collection_numbers):
            return True
        if collection_numbers[position - 1] <= collection_numbers[position]:
            return check_non_decreasing(position + 1)
        return False

    return check_non_decreasing(1)