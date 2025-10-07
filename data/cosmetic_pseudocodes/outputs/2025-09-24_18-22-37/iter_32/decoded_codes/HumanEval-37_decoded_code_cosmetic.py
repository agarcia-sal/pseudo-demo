from typing import List, TypeVar

T = TypeVar('T', bound='SupportsLessThan')


class SupportsLessThan:
    def __lt__(self: T, other: T) -> bool:
        ...


def sort_even(list_of_elements: List[T]) -> List[T]:
    temp_even: List[T] = []
    temp_odd: List[T] = []
    idx_counter: int = 0

    while idx_counter < len(list_of_elements):
        if idx_counter % 2 == 0:
            temp_even.append(list_of_elements[idx_counter])
        else:
            temp_odd.append(list_of_elements[idx_counter])
        idx_counter += 1

    temp_even.sort()

    combined_result: List[T] = []
    pos_in_pair: int = 0
    max_pairs: int = min(len(temp_even), len(temp_odd))

    while pos_in_pair < max_pairs:
        combined_result.append(temp_even[pos_in_pair])
        combined_result.append(temp_odd[pos_in_pair])
        pos_in_pair += 1

    if len(temp_even) > len(temp_odd):
        combined_result.append(temp_even[-1])

    return combined_result