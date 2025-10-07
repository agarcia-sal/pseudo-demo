from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    even_positions: List[T] = []
    position_counter: int = 0
    while position_counter < len(list_of_elements):
        even_positions.append(list_of_elements[position_counter])
        position_counter += 2

    odd_positions: List[T] = []
    index_tracker: int = 1
    while index_tracker < len(list_of_elements):
        odd_positions.append(list_of_elements[index_tracker])
        index_tracker += 2

    even_positions.sort()  # Sort even-positioned elements ascending

    combined_result: List[T] = []
    iterator_i: int = 0
    max_pairs: int = len(odd_positions)
    while iterator_i < max_pairs:
        combined_result.append(even_positions[iterator_i])
        combined_result.append(odd_positions[iterator_i])
        iterator_i += 1

    if len(even_positions) > len(odd_positions):
        combined_result.append(even_positions[-1])

    return combined_result