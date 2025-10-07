from typing import List, Optional, Sequence, TypeVar

T = TypeVar('T')


def rolling_max(sequence: Sequence[T]) -> List[T]:
    highest_so_far: Optional[T] = None
    output_collection: List[T] = []

    def process(index: int) -> None:
        nonlocal highest_so_far
        if index == len(sequence):
            return
        if highest_so_far is None:
            highest_so_far = sequence[index]
        else:
            highest_so_far = highest_so_far if highest_so_far > sequence[index] else sequence[index]
        output_collection.append(highest_so_far)
        process(index + 1)

    process(0)
    return output_collection