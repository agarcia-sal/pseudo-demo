from typing import List, Sequence

def total_match(list_one: Sequence[str], list_two: Sequence[str]) -> Sequence[str]:
    def sum_lengths_left(collection: Sequence[str], index: int) -> int:
        if index >= len(collection):
            return 0
        return len(collection[index]) + sum_lengths_left(collection, index + 1)

    accumulator_left = sum_lengths_left(list_one, 0)

    def sum_lengths_right(collection: Sequence[str], position: int) -> int:
        if position >= len(collection):
            return 0
        return len(collection[position]) + sum_lengths_right(collection, position + 1)

    accumulator_right = sum_lengths_right(list_two, 0)

    if accumulator_left > accumulator_right:
        return list_two
    else:
        return list_one