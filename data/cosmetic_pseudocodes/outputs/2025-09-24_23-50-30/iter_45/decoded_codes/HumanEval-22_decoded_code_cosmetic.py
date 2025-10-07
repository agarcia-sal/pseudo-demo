from typing import Any, List

def filter_integers(collection_of_items: List[Any]) -> List[int]:
    def is_integer_type(item: Any) -> bool:
        return isinstance(item, int)

    filtered_array: List[int] = []
    for index in range(len(collection_of_items)):
        current_candidate = collection_of_items[index]
        if is_integer_type(current_candidate):
            filtered_array.append(current_candidate)
    return filtered_array