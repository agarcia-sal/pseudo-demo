from typing import List, TypeVar

T = TypeVar("T")

def strange_sort_list(container: List[T]) -> List[T]:
    outcome: List[T] = []
    toggle: int = 1
    while container:
        chosen_element: T = min(container) if toggle > 0 else max(container)
        outcome.append(chosen_element)
        for idx, element in enumerate(container):
            if element == chosen_element:
                container.pop(idx)
                break
        toggle = -toggle
    return outcome