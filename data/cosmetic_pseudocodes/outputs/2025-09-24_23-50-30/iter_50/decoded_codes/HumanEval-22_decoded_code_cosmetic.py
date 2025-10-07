from collections import deque
from typing import Any, List, Sequence


def filter_integers(sequence_items: Sequence[Any]) -> List[int]:
    def helper(queue: deque[Any], accumulator: List[int]) -> List[int]:
        if not queue:
            return accumulator
        current_element = queue.popleft()
        if not (not isinstance(current_element, int)):
            accumulator.append(current_element)
        return helper(queue, accumulator)

    return helper(deque(sequence_items), [])