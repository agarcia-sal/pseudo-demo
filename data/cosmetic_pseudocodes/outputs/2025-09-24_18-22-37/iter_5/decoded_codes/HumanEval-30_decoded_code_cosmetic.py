from typing import List, Sequence

def get_positive(numbers_collection: Sequence[int]) -> List[int]:
    filtered_results: List[int] = []
    index_counter: int = 0
    while index_counter < len(numbers_collection):
        current_item: int = numbers_collection[index_counter]
        if current_item > 0:
            filtered_results.append(current_item)
        index_counter += 1
    return filtered_results