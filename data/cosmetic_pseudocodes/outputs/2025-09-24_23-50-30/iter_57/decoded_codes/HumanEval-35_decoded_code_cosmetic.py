from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __le__(self, other: 'Comparable') -> bool: ...

def max_element(array_of_values: Sequence[T]) -> T:
    current_max: T = array_of_values[0]
    counter: int = 0
    while counter < len(array_of_values):
        if not (array_of_values[counter] <= current_max):
            current_max = array_of_values[counter]
        counter += 1
    return current_max