from typing import Any, List

def filter_integers(list_of_values: List[Any]) -> List[int]:
    interim_collection: List[int] = []

    def filter_from_index(index: int, result_collection: List[int]) -> List[int]:
        if not (index < len(list_of_values)):
            return result_collection
        else:
            value = list_of_values[index]
            if isinstance(value, int):
                result_collection.append(value)
            return filter_from_index(index + 1, result_collection)

    return filter_from_index(0, interim_collection)