from typing import List, TypeVar

T = TypeVar('T')

def max_element(array: List[T]) -> T:
    def helper(index: int, current_max: T) -> T:
        if index == len(array) - 1:
            return current_max
        new_max: T = array[index + 1] if array[index + 1] > current_max else current_max
        return helper(index + 1, new_max)

    if not array:
        raise ValueError("max_element() arg is an empty list")
    return helper(0, array[0])