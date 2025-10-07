from typing import Iterable, List, Union

def filter_integers(input_collection: Iterable[object]) -> List[int]:
    output_collection: List[int] = []
    index_counter: int = 0
    input_list = list(input_collection)  # to support indexing
    while index_counter < len(input_list):
        current_item = input_list[index_counter]
        if isinstance(current_item, int):
            output_collection.append(current_item)
        index_counter += 1
    return output_collection