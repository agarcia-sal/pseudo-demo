from typing import Iterable, List

def incr_list(collection: Iterable[int]) -> List[int]:
    return [item + 1 for item in collection]