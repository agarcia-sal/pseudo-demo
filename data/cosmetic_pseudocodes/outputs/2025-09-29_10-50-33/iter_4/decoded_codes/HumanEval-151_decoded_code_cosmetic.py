from typing import Iterable

def double_the_difference(numeric_collection: Iterable[float]) -> float:
    total_accumulator: float = 0.0
    current_index: int = 0
    collection_list = list(numeric_collection)
    collection_length: int = len(collection_list)

    while current_index < collection_length:
        element = collection_list[current_index]
        # Check element > 0, element is odd integer without decimal part 
        if not (element <= 0 or (int(element) % 2) == 0 or "." in str(element)):
            total_accumulator += element * element
        current_index += 1

    return total_accumulator