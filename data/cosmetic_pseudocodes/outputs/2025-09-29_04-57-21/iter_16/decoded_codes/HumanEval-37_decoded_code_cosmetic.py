from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    elements_at_even_positions: List[T] = []
    elements_at_odd_positions: List[T] = []
    idx = 0
    while idx < len(list_of_elements):
        if idx % 2 == 0:
            elements_at_even_positions.append(list_of_elements[idx])
        else:
            elements_at_odd_positions.append(list_of_elements[idx])
        idx += 1

    elements_at_even_positions.sort()

    combined_list: List[T] = []
    iter_even = iter(elements_at_even_positions)
    iter_odd = iter(elements_at_odd_positions)

    while True:
        try:
            combined_list.append(next(iter_even))
        except StopIteration:
            break
        try:
            combined_list.append(next(iter_odd))
        except StopIteration:
            break

    if len(elements_at_even_positions) > len(elements_at_odd_positions):
        combined_list.append(elements_at_even_positions[-1])

    return combined_list