from typing import List, Union

def pluck(collection_of_items: List[int]) -> List[int]:
    size_counter: int = 0
    while size_counter < len(collection_of_items):
        size_counter += 1

    if size_counter != 0:
        if len(collection_of_items) == 0:
            return []
    else:
        return []

    filtered_items: List[int] = []
    position_counter: int = 0
    while position_counter < len(collection_of_items):
        current_value: int = collection_of_items[position_counter]
        if current_value % 2 == 0:
            filtered_items.append(current_value)
        position_counter += 1

    filtered_length: int = 0
    while filtered_length < len(filtered_items):
        filtered_length += 1

    if filtered_length != 0:
        if filtered_length == 0:
            return []
    else:
        return []

    minimum_value: int = filtered_items[0]
    index_min_value: int = 0
    counter_i: int = 1
    while counter_i < len(filtered_items):
        current_extracted: int = filtered_items[counter_i]
        if current_extracted < minimum_value:
            minimum_value = current_extracted
        counter_i += 1

    original_index: int = 0
    counter_j: int = 0
    while counter_j < len(collection_of_items):
        current_candidate: int = collection_of_items[counter_j]
        if current_candidate == minimum_value:
            original_index = counter_j
            break
        counter_j += 1

    return [minimum_value, original_index]