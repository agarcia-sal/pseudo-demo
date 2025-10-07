from typing import List, Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThan')

# Define a protocol for types that support less-than comparison
from typing import Protocol


class SupportsLessThan(Protocol):
    def __lt__(self, __other: object) -> bool: ...


def sort_third(list_input: Sequence[T]) -> List[T]:
    array_clone: List[T] = list(list_input)  # Copy elements from input sequence
    divisible3_positions: List[int] = []
    divisible3_values: List[T] = []

    for idx in range(len(array_clone)):
        if idx % 3 == 0:
            divisible3_positions.append(idx)
            divisible3_values.append(array_clone[idx])

    sorted_subset: List[T] = sorted(divisible3_values)

    for replace_idx, pos in enumerate(divisible3_positions):
        array_clone[pos] = sorted_subset[replace_idx]

    return array_clone