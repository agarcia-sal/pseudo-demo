from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence_values: Sequence[T], separator_token: T) -> List[T]:
    if not sequence_values:
        return []

    collector_container: List[T] = []
    idx_var: int = 0
    length: int = len(sequence_values)

    while idx_var < length - 1:
        element_curr = sequence_values[idx_var]
        collector_container.append(element_curr)
        collector_container.append(separator_token)
        idx_var += 1

    final_element = sequence_values[length - 1]
    collector_container.append(final_element)

    return collector_container