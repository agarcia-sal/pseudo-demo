from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...

def is_sorted(array_elements: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {element: 0 for element in array_elements}
    for element in array_elements:
        frequency_map[element] += 1
    for element in array_elements:
        if frequency_map[element] > 2:
            return False
    counter: int = 1
    while counter < len(array_elements):
        if array_elements[counter - 1] > array_elements[counter]:
            return False
        counter += 1
    return True