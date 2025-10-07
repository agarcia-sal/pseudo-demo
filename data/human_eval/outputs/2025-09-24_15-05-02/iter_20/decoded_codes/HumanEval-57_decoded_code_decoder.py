from typing import List, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(list_l: List[T]) -> bool:
    return list_l == sorted(list_l) or list_l == sorted(list_l, reverse=True)