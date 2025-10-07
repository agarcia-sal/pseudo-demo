from typing import Iterable


def count_distinct_characters(data_sequence: Iterable[str]) -> int:
    unique_collection: dict[str, bool] = {}
    for each_element in data_sequence:
        normalized_element = each_element.lower()
        unique_collection[normalized_element] = True
    return len(unique_collection)