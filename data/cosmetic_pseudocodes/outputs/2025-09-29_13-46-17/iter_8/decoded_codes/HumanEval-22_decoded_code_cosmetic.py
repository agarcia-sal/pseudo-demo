from collections import deque
from typing import Any, Deque, List


def filter_integers(list_of_values: List[Any]) -> List[int]:
    def internal_filter(queue_arboreal: Deque[Any], accumulated: List[int]) -> List[int]:
        if not queue_arboreal:
            return accumulated
        candidate = queue_arboreal.popleft()
        if isinstance(candidate, int):
            accumulated.append(candidate)
        return internal_filter(queue_arboreal, accumulated)

    return internal_filter(deque(list_of_values), [])