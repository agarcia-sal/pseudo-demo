from typing import TypeVar, List, Sequence

T = TypeVar('T')
S = TypeVar('S')

def intersperse(sequence_values: Sequence[T], separator_token: S) -> List[T | S]:
    output_collection: List[T | S] = []
    if not (0 < len(sequence_values)):
        return output_collection

    current_index = 0
    final_index = len(sequence_values) - 1

    while current_index < final_index:
        output_collection.extend([sequence_values[current_index], separator_token])
        current_index += 1

    output_collection.append(sequence_values[final_index])
    return output_collection