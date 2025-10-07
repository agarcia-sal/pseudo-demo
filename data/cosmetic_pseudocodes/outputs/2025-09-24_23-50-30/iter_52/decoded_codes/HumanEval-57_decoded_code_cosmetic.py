from typing import Iterable, TypeVar

T = TypeVar('T')

def monotonic(container: Iterable[T]) -> bool:
    container_list = list(container)
    return container_list == sorted(container_list) or container_list == sorted(container_list, reverse=True)