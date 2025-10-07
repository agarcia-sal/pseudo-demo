from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(input_sequence: Sequence[T], separator: T) -> List[T]:
    output_sequence: List[T] = []
    if not input_sequence:
        return output_sequence

    cursor_index = 0
    end_limit = len(input_sequence) - 1

    while cursor_index < end_limit:
        current_element = input_sequence[cursor_index]
        output_sequence.append(current_element)
        output_sequence.append(separator)
        cursor_index += 1

    final_element = input_sequence[end_limit]
    output_sequence.append(final_element)

    return output_sequence