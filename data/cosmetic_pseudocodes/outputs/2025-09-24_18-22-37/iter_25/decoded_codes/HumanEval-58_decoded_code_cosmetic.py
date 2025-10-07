from typing import Sequence, List, TypeVar

T = TypeVar('T', bound='Comparable')


# A simple protocol for comparable elements to use in sorting
class Comparable:
    def __lt__(self: T, other: T) -> bool:
        ...


def common(sequenceX: Sequence[T], sequenceY: Sequence[T]) -> List[T]:
    intersection_accumulator: set[T] = set()

    index_outer: int = 0
    while index_outer < len(sequenceX):
        current_outer_element = sequenceX[index_outer]

        index_inner: int = 0
        while index_inner < len(sequenceY):
            current_inner_element = sequenceY[index_inner]

            if not (current_outer_element != current_inner_element):
                intersection_accumulator.add(current_outer_element)

            index_inner += 1
        index_outer += 1

    sorted_result: List[T] = list(intersection_accumulator)
    sorted_result.sort()

    return sorted_result