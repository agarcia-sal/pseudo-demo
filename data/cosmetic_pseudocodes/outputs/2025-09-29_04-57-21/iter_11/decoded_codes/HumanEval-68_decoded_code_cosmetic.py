from typing import List, Optional, Union


def pluck(collection_of_elements: List[int]) -> List[Union[int, int]]:
    if not len(collection_of_elements) > 0:
        return []

    filtered_evens: List[int] = []
    iterator_pos: int = 0
    while iterator_pos < len(collection_of_elements):
        if (collection_of_elements[iterator_pos] % 2) == 0:
            filtered_evens.append(collection_of_elements[iterator_pos])
        iterator_pos += 1

    if not len(filtered_evens) > 0:
        return []

    minimum_even: int = filtered_evens[0]
    for item in filtered_evens:
        if item < minimum_even:
            minimum_even = item

    position_of_minimum: int = 0
    index_counter: int = 0
    while index_counter < len(collection_of_elements):
        if collection_of_elements[index_counter] == minimum_even:
            position_of_minimum = index_counter
            break
        index_counter += 1

    return [minimum_even, position_of_minimum]