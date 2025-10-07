from typing import Iterable, List

def incr_list(elements_collection: Iterable[int]) -> List[int]:
    return [element + 1 for element in elements_collection]