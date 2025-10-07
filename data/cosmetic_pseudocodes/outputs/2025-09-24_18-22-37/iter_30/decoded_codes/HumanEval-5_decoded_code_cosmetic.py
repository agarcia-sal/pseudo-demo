from typing import Sequence, TypeVar, List

T = TypeVar('T')
S = TypeVar('S')

def intersperse(sequence_of_values: Sequence[T], separator_symbol: S) -> List[T | S]:
    if len(sequence_of_values) == 0:
        return []
    accumulated_result: List[T | S] = []
    position_index = 0
    while position_index < len(sequence_of_values) - 1:
        current_entry = sequence_of_values[position_index]
        accumulated_result.append(current_entry)
        accumulated_result.append(separator_symbol)
        position_index += 1
    final_element = sequence_of_values[-1]
    accumulated_result.append(final_element)
    return accumulated_result