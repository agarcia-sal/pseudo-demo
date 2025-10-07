from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def helper_fn(idx_Alpha: int, curr_max: T) -> T:
        if idx_Alpha >= len(list_of_elements):
            return curr_max
        valOmega = list_of_elements[idx_Alpha]
        new_maximum_1b3 = valOmega if valOmega > curr_max else curr_max
        return helper_fn(idx_Alpha + 1, new_maximum_1b3)
    return helper_fn(0, list_of_elements[0])