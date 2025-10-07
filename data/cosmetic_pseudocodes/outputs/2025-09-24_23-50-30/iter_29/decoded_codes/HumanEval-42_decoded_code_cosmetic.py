from typing import Iterable, List

def incr_list(input_collection: Iterable[int]) -> List[int]:
    return [unit + 1 for unit in input_collection]