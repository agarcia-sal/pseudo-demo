from typing import List, Sized, TypeVar

T = TypeVar('T', bound=Sized)

def total_match(original_array: List[T], secondary_array: List[T]) -> List[T]:
    sum_first: int = 0
    index_counter: int = 0
    while index_counter < len(original_array):
        sum_first += len(original_array[index_counter])
        index_counter += 1

    sum_second: int = 0
    for position in range(len(secondary_array)):
        sum_second += len(secondary_array[position])

    if not (sum_first > sum_second):
        return original_array
    return secondary_array