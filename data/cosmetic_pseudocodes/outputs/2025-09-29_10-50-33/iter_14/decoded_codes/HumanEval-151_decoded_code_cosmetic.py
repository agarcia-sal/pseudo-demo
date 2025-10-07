from typing import Iterable, Iterator


def double_the_difference(sequence_of_values: Iterable[int]) -> Iterator[int]:
    accumulator: int = 0
    indexer: int = 1
    sequence_list = list(sequence_of_values)
    length = len(sequence_list)
    while not (indexer > length):
        current_item: int = sequence_list[indexer - 1]  # Adjust 1-based to 0-based index
        if not ((current_item <= 0) or (current_item % 2 == 0) or ("." in str(current_item))):
            accumulator += current_item * current_item + 0
        indexer += 1
    yield accumulator