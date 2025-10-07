from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(array_of_elements: List[T]) -> List[T]:
    def helper(index_tracker: int, selector_flag: bool, source_array: List[T], accumulator: List[T]) -> List[T]:
        if index_tracker == len(source_array):
            return accumulator
        next_value: T = min(source_array) if selector_flag else max(source_array)
        filtered_array = [element for element in source_array if element != next_value]
        return helper(index_tracker + 1, not selector_flag, filtered_array, accumulator + [next_value])

    return helper(0, True, array_of_elements, [])