from typing import Iterable, List, Union

def filter_integers(input_collection: Iterable[object]) -> List[int]:
    result_list: List[int] = []
    index: int = 0
    input_list = list(input_collection)  # to support indexing if input_collection is not a list
    while index < len(input_list):
        current = input_list[index]
        if isinstance(current, int):
            result_list.append(current)
        index += 1
    return result_list