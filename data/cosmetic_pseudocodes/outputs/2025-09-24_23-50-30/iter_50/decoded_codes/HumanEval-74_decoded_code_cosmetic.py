from typing import List, Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(list_one: List[Sequence], list_two: List[Sequence]) -> List[Sequence]:
    def sum_lengths_iter(collection: List[Sequence], idx: int, acc: int) -> int:
        if not (idx < len(collection)):
            return acc
        else:
            return sum_lengths_iter(collection, idx + 1, acc + len(collection[idx]))

    aggregate_one: int = sum_lengths_iter(list_one, 0, 0)
    aggregate_two: int = sum_lengths_iter(list_two, 0, 0)

    if aggregate_one <= aggregate_two:
        return list_one
    else:
        return list_two