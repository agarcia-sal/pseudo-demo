from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    elements_at_even_positions: List[T] = []
    elements_at_odd_positions: List[T] = []
    index_counter: int = 0

    for element in list_of_elements:
        if index_counter % 2 == 0:
            elements_at_even_positions.append(element)
        else:
            elements_at_odd_positions.append(element)
        index_counter += 1

    elements_at_even_positions.sort()

    combined_result: List[T] = []
    combined_index: int = 0
    max_pairs: int = min(len(elements_at_even_positions), len(elements_at_odd_positions))

    while combined_index < max_pairs:
        combined_result.append(elements_at_even_positions[combined_index])
        combined_result.append(elements_at_odd_positions[combined_index])
        combined_index += 1

    if len(elements_at_even_positions) > len(elements_at_odd_positions):
        combined_result.append(elements_at_even_positions[-1])

    return combined_result