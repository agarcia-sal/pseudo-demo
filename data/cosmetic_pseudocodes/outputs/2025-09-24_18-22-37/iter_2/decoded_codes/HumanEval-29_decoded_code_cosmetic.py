from typing import Iterable, List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence[str])

def filter_by_prefix(collection: Iterable[str], prefix: str) -> List[str]:
    return [element for element in collection if element[:len(prefix)] == prefix]