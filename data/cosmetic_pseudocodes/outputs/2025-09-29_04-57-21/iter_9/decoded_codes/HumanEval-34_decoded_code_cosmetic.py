from typing import TypeVar, List, Callable

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    distinct_values: List[T] = []
    unique_checker: set[T] = set()

    position = 0
    while position < len(list_of_elements):
        current_element = list_of_elements[position]
        if current_element not in unique_checker:
            distinct_values.append(current_element)
            unique_checker.add(current_element)
        position += 1

    def comparator(a: T, b: T) -> bool:
        return a < b

    # Python's sort does not use comparator that returns bool, so we sort naturally
    return sorted(distinct_values)