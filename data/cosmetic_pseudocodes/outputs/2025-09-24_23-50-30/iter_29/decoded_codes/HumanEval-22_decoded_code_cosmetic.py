from typing import Iterable, List

def filter_integers(data_collection: Iterable[object]) -> List[int]:
    result_list: List[int] = []
    for item in data_collection:
        if isinstance(item, int):
            result_list.append(item)
    return result_list