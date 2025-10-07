from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

def monotonic(xqro: Sequence[T]) -> bool:
    sorted_xqro = sorted(xqro)
    return xqro == sorted_xqro or xqro == sorted_xqro[::-1]