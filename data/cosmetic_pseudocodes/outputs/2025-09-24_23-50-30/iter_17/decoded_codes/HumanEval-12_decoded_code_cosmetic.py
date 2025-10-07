from typing import Sequence, Optional, Any

def longest(collection_of_items: Sequence[Sequence[Any]]) -> Optional[Sequence[Any]]:
    if not collection_of_items:
        return None

    lengths_dictionary = {index: len(collection_of_items[index]) for index in range(len(collection_of_items))}

    highest_value = float('-inf')
    for length in lengths_dictionary.values():
        if length > highest_value:
            highest_value = length

    for position in range(len(collection_of_items)):
        if len(collection_of_items[position]) == highest_value:
            return collection_of_items[position]