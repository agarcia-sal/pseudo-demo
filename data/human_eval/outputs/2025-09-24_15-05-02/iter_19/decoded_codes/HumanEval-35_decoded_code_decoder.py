from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __gt__(self, other: 'Comparable') -> bool: ...

def max_element(list_of_elements: List[T]) -> T:
    maximum_value: T = list_of_elements[0]
    for element in list_of_elements:
        if element > maximum_value:
            maximum_value = element
    return maximum_value