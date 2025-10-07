from typing import Iterable, List, Sequence, TypeVar

T = TypeVar("T", bound=Sequence[str])

def filter_by_prefix(collection: Iterable[T], start_seq: Sequence[str]) -> List[T]:
    return [item for item in collection if item[:len(start_seq)] == start_seq]