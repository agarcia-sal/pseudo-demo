from typing import List, Any

def sort_even(list_of_elements: List[Any]) -> List[Any]:
    evens_collection: List[Any] = []
    odds_collection: List[Any] = []

    def partition_elements(index: int) -> None:
        if index >= len(list_of_elements):
            return
        if index % 2 == 0:
            evens_collection.append(list_of_elements[index])
        else:
            odds_collection.append(list_of_elements[index])
        partition_elements(index + 1)

    partition_elements(0)

    evens_collection.sort()

    merged_result: List[Any] = []

    def merge_pairs(position: int) -> None:
        if position >= min(len(evens_collection), len(odds_collection)):
            return
        merged_result.extend([evens_collection[position], odds_collection[position]])
        merge_pairs(position + 1)

    merge_pairs(0)

    if len(evens_collection) > len(odds_collection):
        merged_result.append(evens_collection[-1])

    return merged_result