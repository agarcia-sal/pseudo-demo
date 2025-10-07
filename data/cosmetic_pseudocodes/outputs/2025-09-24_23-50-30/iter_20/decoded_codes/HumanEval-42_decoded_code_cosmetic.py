from typing import Iterable, List

def incr_list(collection: Iterable[int]) -> List[int]:
    result_set = {item + 1 for item in collection}
    return list(result_set)