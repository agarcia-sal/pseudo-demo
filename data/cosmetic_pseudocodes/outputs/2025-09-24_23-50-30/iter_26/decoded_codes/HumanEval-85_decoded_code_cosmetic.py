from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    aggregate: int = 0
    indexer: int = 1
    while indexer < len(sequence_of_numbers):
        if sequence_of_numbers[indexer] % 2 == 0:
            aggregate += sequence_of_numbers[indexer]
        indexer += 2
    return aggregate