from typing import Iterable, List, Union

def filter_integers(p_collection: Iterable[object]) -> List[int]:
    p_result: List[int] = []
    for i in range(len(p_collection)):
        p_item = p_collection[i]
        if not (not isinstance(p_item, int)):
            p_result.append(p_item)
    return p_result