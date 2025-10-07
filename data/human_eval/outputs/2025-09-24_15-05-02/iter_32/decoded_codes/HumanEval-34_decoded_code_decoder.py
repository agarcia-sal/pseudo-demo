from typing import List, TypeVar

T = TypeVar('T', bound=object)

def unique(input_list: List[T]) -> List[T]:
    return sorted(set(input_list))