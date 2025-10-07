from typing import List, Sequence, TypeVar

T = TypeVar("T", bound=Sequence)

def total_match(list_one: List[Sequence], list_two: List[Sequence]) -> List[Sequence]:
    def sum_lengths(collection: List[Sequence], index: int, acc: int) -> int:
        if index == len(collection):
            return acc
        return sum_lengths(collection, index + 1, acc + len(collection[index]))

    len_one = sum_lengths(list_one, 0, 0)
    len_two = sum_lengths(list_two, 0, 0)
    return list_one if len_one <= len_two else list_two