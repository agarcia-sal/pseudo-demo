from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_collection: Iterable[T]) -> List[T]:
    temp_set = {x for x in input_collection}
    temp_list = [y for y in temp_set]
    return sorted(temp_list)