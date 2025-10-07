from typing import List, TypeVar

T = TypeVar('T')

def intersperse(sequence_array: List[T], separator_token: T) -> List[T]:
    if len(sequence_array) == 0:
        return []

    output_array: List[T] = []

    iterator_index: int = 0
    while iterator_index < len(sequence_array) - 1:
        current_element: T = sequence_array[iterator_index]
        output_array.append(current_element)
        output_array.append(separator_token)
        iterator_index += 1

    terminal_element: T = sequence_array[-1]
    output_array.append(terminal_element)

    return output_array