from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(collection_of_values: Iterable[T], separator_symbol: T) -> List[T]:
    # Count the length manually as in pseudocode
    source_length: int = 0
    for _ in collection_of_values:
        source_length += 1

    if source_length != 0:
        outcome_container: List[T] = []
        limit_index: int = source_length - 1
        current_pointer: int = 0

        # Convert collection to a sequence to have O(1) access via index
        sequence = list(collection_of_values)

        while current_pointer < limit_index:
            temp_value_one: T = sequence[current_pointer]
            outcome_container.append(temp_value_one)

            temp_value_two: T = separator_symbol
            outcome_container.append(temp_value_two)

            current_pointer += 1

        temp_value_one = sequence[limit_index]
        outcome_container.append(temp_value_one)

        return outcome_container

    return []