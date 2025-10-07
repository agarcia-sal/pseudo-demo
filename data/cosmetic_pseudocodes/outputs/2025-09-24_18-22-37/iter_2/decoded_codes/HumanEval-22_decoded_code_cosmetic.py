from typing import Any, List


def filter_integers(input_array: List[Any]) -> List[int]:
    result_collection: List[int] = []
    for each_item in input_array:
        if isinstance(each_item, int):
            result_collection.append(each_item)
    return result_collection