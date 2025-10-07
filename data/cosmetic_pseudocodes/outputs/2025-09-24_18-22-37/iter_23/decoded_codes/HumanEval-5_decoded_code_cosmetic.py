from typing import List, TypeVar

T = TypeVar('T')

def intersperse(array_values: List[T], sep_token: T) -> List[T]:
    output_sequence: List[T] = []
    idx_counter: int = 0

    if array_values:
        while idx_counter < len(array_values) - 1:
            current_item: T = array_values[idx_counter]
            output_sequence.append(current_item)
            output_sequence.append(sep_token)
            idx_counter += 1

        final_entry: T = array_values[-1]
        output_sequence.append(final_entry)

        return output_sequence
    else:
        return []