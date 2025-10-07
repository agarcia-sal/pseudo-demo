from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    primary_positions: List[T] = []
    secondary_positions: List[T] = []
    current_index: int = 0
    total_size: int = len(list_of_elements)

    while current_index < total_size:
        primary_positions.append(list_of_elements[current_index])
        current_index += 2

    alternative_index: int = 1
    while alternative_index < total_size:
        secondary_positions.append(list_of_elements[alternative_index])
        alternative_index += 2

    primary_positions.sort()

    combined_result: List[T] = []
    pair_index: int = 0
    limit: int = len(secondary_positions)

    while pair_index < limit:
        combined_result.append(primary_positions[pair_index])
        combined_result.append(secondary_positions[pair_index])
        pair_index += 1

    if len(primary_positions) > len(secondary_positions):
        combined_result.append(primary_positions[-1])

    return combined_result