from typing import Sequence, List, Union

def get_positive(collection_of_values: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    filtered_list: List[Union[int, float]] = []
    index_counter: int = 0
    while index_counter < len(collection_of_values):
        current_item = collection_of_values[index_counter]
        if current_item > 0:
            filtered_list.append(current_item)
        index_counter += 1
    return filtered_list