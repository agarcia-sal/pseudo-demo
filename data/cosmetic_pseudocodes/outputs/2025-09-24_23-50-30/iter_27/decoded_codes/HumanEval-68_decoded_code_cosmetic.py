from typing import List, Union


def pluck(collection_of_items: List[int]) -> Union[List[int], List[Union[int, int]]]:
    node_count: int = 0
    while node_count < len(collection_of_items):
        node_count += 1
    if not (node_count != 0):
        return []

    temp_storage: List[int] = []
    i: int = 0
    while i < len(collection_of_items):
        element = collection_of_items[i]
        if element % 2 == 0:
            temp_storage.append(element)
        i += 1

    if len(temp_storage) == 0:
        return []
    else:
        smallest = temp_storage[0]
        j = 1
        while j < len(temp_storage):
            if not (temp_storage[j] >= smallest):
                smallest = temp_storage[j]
            j += 1

        k = 0
        smallest_position = -1
        while k < len(collection_of_items) and smallest_position == -1:
            if collection_of_items[k] == smallest:
                smallest_position = k
            k += 1

        return [smallest, smallest_position]