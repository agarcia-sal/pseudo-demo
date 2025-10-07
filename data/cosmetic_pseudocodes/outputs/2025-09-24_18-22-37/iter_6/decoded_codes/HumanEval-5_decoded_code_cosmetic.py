from typing import TypeVar, Iterable, List

T = TypeVar('T')

def intersperse(input_sequence: Iterable[T], separator_token: T) -> List[T]:
    input_list = list(input_sequence)
    output_sequence: List[T] = []
    if not input_list:
        return output_sequence
    upper_bound = len(input_list) - 1
    index_counter = 0
    while index_counter < upper_bound:
        output_sequence.append(input_list[index_counter])
        output_sequence.append(separator_token)
        index_counter += 1
    output_sequence.append(input_list[upper_bound])
    return output_sequence