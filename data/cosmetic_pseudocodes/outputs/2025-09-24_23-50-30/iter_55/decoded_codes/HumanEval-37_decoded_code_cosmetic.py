from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    acc: List[T] = []
    even_positions: List[T] = []
    odd_positions: List[T] = []
    idx: int = 0
    while idx < len(list_of_elements):
        if idx % 2 == 0:
            even_positions.append(list_of_elements[idx])
        else:
            odd_positions.append(list_of_elements[idx])
        idx += 1
    even_positions.sort()  # Sort even positions ascending
    combined_length = len(even_positions) + len(odd_positions)
    iterator_even = 0
    iterator_odd = 0
    while len(acc) < combined_length:
        if len(acc) % 2 == 0:
            acc.append(even_positions[iterator_even])
            iterator_even += 1
        else:
            acc.append(odd_positions[iterator_odd])
            iterator_odd += 1
    return acc