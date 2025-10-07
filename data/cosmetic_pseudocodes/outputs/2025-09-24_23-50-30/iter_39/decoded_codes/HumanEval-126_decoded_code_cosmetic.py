from typing import Sequence, Dict


def is_sorted(collection_numbers: Sequence[int]) -> bool:
    dict_counts: Dict[int, int] = {}

    for element in collection_numbers:
        if element not in dict_counts:
            dict_counts[element] = 0

    def accumulate(index: int, dict_current: Dict[int, int]) -> Dict[int, int]:
        if index == len(collection_numbers):
            return dict_current
        value_curr = collection_numbers[index]
        dict_current[value_curr] += 1
        return accumulate(index + 1, dict_current)

    dict_counts = accumulate(0, dict_counts)

    for key in collection_numbers:
        if dict_counts[key] > 2:
            return False

    def check_order(position: int) -> bool:
        if position == len(collection_numbers):
            return True
        if collection_numbers[position - 1] > collection_numbers[position]:
            return False
        return check_order(position + 1)

    return check_order(1)