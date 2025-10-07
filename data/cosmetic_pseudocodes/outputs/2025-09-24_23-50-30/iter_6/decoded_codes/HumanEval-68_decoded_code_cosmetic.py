from typing import List, Union

def pluck(collection: List[int]) -> Union[List[int], List[int]]:
    if len(collection) == 0:
        return []

    filtered: List[int] = []
    position = 0
    while position < len(collection):
        item = collection[position]
        if item - 2 * (item // 2) == 0:  # Check if item is even
            filtered.append(item)
        position += 1

    if len(filtered) == 0:
        return []

    minimum_value = filtered[0]
    for element in filtered:
        if element - minimum_value < 0:
            minimum_value = element

    found_index = 0
    while found_index < len(collection):
        if collection[found_index] == minimum_value:
            break
        found_index += 1

    return [minimum_value, found_index]