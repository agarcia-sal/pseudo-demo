from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(input_sequence: Iterable[T], separator: T) -> List[T]:
    input_list = list(input_sequence)
    if not input_list:
        return []
    output_sequence: List[T] = []
    iterator = 0
    while iterator < len(input_list) - 1:
        output_sequence.append(input_list[iterator])
        output_sequence.append(separator)
        iterator += 1
    output_sequence.append(input_list[-1])
    return output_sequence