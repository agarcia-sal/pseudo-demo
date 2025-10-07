from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection_of_entities: Sequence[T]) -> T:
    if not collection_of_entities:
        raise ValueError("max_element() arg is an empty sequence")

    peak_value: T = collection_of_entities[0]
    position_counter: int = 0
    total_count: int = len(collection_of_entities)

    while position_counter < total_count:
        candidate: T = collection_of_entities[position_counter]

        if candidate > peak_value:
            peak_value = candidate
        # No operation needed for default case

        position_counter += 1

    return peak_value