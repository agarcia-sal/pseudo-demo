from collections.abc import Sequence
from typing import Iterable, TypeVar

T = TypeVar("T")

def monotonic(input_collection: Iterable[T]) -> bool:
    seq = list(input_collection)
    return seq == sorted(seq) or seq == sorted(seq, reverse=True)