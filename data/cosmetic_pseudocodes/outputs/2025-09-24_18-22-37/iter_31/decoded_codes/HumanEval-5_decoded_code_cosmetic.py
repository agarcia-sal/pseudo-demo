from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(input_sequence: Iterable[T], separator: T) -> List[T]:
    output_container: List[T] = []
    input_list = list(input_sequence)
    if input_list:
        sequence_limit = len(input_list) - 1
        iterator_index = 0
        while iterator_index < sequence_limit:
            current_element = input_list[iterator_index]
            output_container.append(current_element)
            output_container.append(separator)
            iterator_index += 1
        final_element = input_list[-1]
        output_container.append(final_element)
    else:
        output_container = []
    return output_container