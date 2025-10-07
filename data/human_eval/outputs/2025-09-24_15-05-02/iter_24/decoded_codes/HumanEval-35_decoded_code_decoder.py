from typing import List, TypeVar

T = TypeVar('T', bound='SupportsComparison')

def max_element(list_l: List[T]) -> T:
    if not list_l:
        raise ValueError("max_element() arg is an empty list")
    m = list_l[0]
    for e in list_l:
        if e > m:
            m = e
    return m


# To support generic type hinting for elements that support comparison
from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportsComparison(Protocol):
    def __gt__(self, __other: object) -> bool: ...