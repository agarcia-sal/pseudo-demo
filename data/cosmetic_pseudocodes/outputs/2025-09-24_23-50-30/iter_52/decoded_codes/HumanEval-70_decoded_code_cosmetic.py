from typing import List, TypeVar, Callable

T = TypeVar('T')

def strange_sort_list(container: List[T]) -> List[T]:
    output: List[T] = []
    toggle: bool = False

    def process(input_collection: List[T], accumulator: List[T], flag: bool) -> List[T]:
        if not input_collection:
            return accumulator
        chosen_element: T = max(input_collection) if flag else min(input_collection)
        accumulator.append(chosen_element)
        filtered_collection: List[T] = [elem for elem in input_collection if elem != chosen_element]
        return process(filtered_collection, accumulator, not flag)

    return process(container, output, toggle)