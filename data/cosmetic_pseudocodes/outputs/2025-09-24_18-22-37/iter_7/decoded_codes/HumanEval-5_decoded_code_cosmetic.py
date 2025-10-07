from typing import List, TypeVar, Iterable

T = TypeVar('T')

def intersperse(collection_of_values: Iterable[T], separator: T) -> List[T]:
    combined_sequence: List[T] = []
    values = list(collection_of_values)

    while values:
        position_counter = 0
        total_items = len(values)

        if position_counter == total_items - 1:
            # Only one item left
            current_value = values[position_counter]
            combined_sequence.append(current_value)
            values = []
        else:
            while position_counter < total_items - 1:
                current_value = values[position_counter]
                combined_sequence.append(current_value)

                combined_sequence.append(separator)
                position_counter += 1

            final_value = values[total_items - 1]
            combined_sequence.append(final_value)
            values = []

    return combined_sequence